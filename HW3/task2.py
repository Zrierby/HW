from functools import wraps


def cache(times=2):
    def cache_decorator(func):
        memor = {}
        count_dic = {}

        @wraps(func)
        def wrapper(*args):
            if args in count_dic and count_dic[args] < times:
                count_dic[args] += 1
                print(' cached value: ')
                return memor[args]
            else:
                if args in count_dic and count_dic[args] >= times:
                    memor.pop(args)
                count_dic[args] = 0
                initial_func_result = func(*args)
                memor[args] = initial_func_result
                print(' executed value: ')
                return initial_func_result
        return wrapper
    return cache_decorator


@cache(times=2)
def pow_func(a, b):
    return (a ** b) ** 2