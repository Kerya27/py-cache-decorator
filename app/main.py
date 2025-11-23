from typing import Callable


def cache(func: Callable) -> Callable:

    cache_store = {}

    def wrapper(*args, **kwargs) -> int:

        if args not in cache_store:
            number = func(*args, **kwargs)
            cache_store[args] = number
            print("Calculating new result")
            return number
        else:
            print("Getting from cache")
            return cache_store[args]
    return wrapper
