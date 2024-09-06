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
    if n < 1:
        raise ValueError("Number must be > 1")
    result = []
    counter = 0
    # начинаем с единицы, потому что там начинается поиск всех простых чисел нашей цифры - 1
    # и начинается поиск простых чисел нашей цифры, если число делится на единицу то проверяем как число цифры "самостоятельно" делилось
    while n % 2 == 0:
        counter += 1
        n //= 2
    # т.к. у меня бывает, что 2 отрицательное число выдает ошибку. поэтому начинаем поиск на числа 3 и 5 для убедившейся того,
    # что начали делиться хотя бы по одному разу. иначе получим некорректное решени