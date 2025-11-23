from typing import Callable, Any


def cache(func: Callable) -> Callable:

    cache_store = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args
        if kwargs:
            key = key + tuple(sorted(kwargs.values()))
        if key not in cache_store:
            number = func(*args, **kwargs)
            cache_store[key] = number
            print("Calculating new result")
            return number
        else:
            print("Getting from cache")
            return cache_store[key]
    return wrapper
