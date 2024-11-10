def is_prime(fu):
    def wrapper(*args):
        result = fu(*args)
        for i in range(2, result - 1):
            if result % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
