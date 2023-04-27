from functools import lru_cache
import hashlib
import json

key_cache = {}

@lru_cache(maxsize=10000)
def get_user_data():
    try:
        with open('./users.json', 'r') as f:
             users = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或内容为空，返回空列表
        users = []
    return users


def had_user_key(key):
    if key in key_cache:
        return True
    users = get_user_data()
    for user in users:
        hash_object = hashlib.md5(user['key'].encode())
        md5 = hash_object.hexdigest()
        print(md5)
        if str(md5) == key:
            user['key'] = md5
            key_cache[md5] = "1"
            return True
    return False

def clear_key_cache(key):
    if key in key_cache:
        key_cache.pop(key)