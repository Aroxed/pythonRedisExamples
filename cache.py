import redis

cache = redis.Redis(host='192.168.0.106', port=6379)


def get_data(key):
    data = cache.get(key)
    if data is None:
        data = "Значення відсутнє в кеші"
    return data


def set_data(key, value):
    cache.set(key, value)


def clear_cache():
    cache.flushdb()


clear_cache()
data_from_cache = get_data("cache_data")
print(data_from_cache)
set_data("cache_data", "Hello, World")

data_from_cache = get_data("cache_data")
print(data_from_cache)
