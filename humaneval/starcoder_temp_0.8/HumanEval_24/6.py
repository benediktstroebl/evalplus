

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def recurse(num):
        if num == 1:
            return num
        elif num % 2 == 0:
            return recurse(num // 2)
        else:
            return recurse(num - 1)
    return recurse(n)

