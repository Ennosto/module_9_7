def is_prime(fu):
    def wrapper(*args):
        result = fu(*args)
        prime = True
        for i in range(2, result - 1):
            if result % i == 0:
                prime = False
                break
            else:
                prime = True
        if prime is True:
            print('Простое')
            return result
        else:
            print('Составное')
            return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

Number_2 = sum_three(5, 5, 5)
print(Number_2)

Num_3 = sum_three(8, 8, 8)
print(Num_3)

TWO_TWO = sum_three(1, 1, 0)
print(TWO_TWO)
