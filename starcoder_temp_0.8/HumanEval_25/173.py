from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # YOUR CODE HERE
    # 1. проверка на простое число
    # 2. если число не простое, находим максимальный делитель
    # 3. отнимаем это значение из делителя
    # 4. запускаем пункт 2
    return []
