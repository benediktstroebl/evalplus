

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def is_divisor(x: int, y: int) -> bool:
        """ check if x is a divisor of y"""
        return x % y == 0

    def divisors(y: int) -> List[int]:
        """ returns all divisors of y"""
        divisors = []
        for x in range(1, y + 1):
            if is_divisor(y, x):
                divisors.append(x)
        return divisors

    def smallest_multiple(x: int) -> int:
        """ returns the smallest multiple of x"""
        if x % 2 == 0:
            return x + 1
        else:
            return x

    smallest_multiple_values = [smallest_multiple(x) for x in range(1, n + 1)]
    return max(smallest_multiple_values)
