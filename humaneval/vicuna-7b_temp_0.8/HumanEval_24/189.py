

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def is_divisor(m, n):
        if m == 0:
            return False
        elif n % m == 0:
            return True
        elif n // m == 0:
            return True
        else:
            return False

    # base case: if n is 1, return 1
    if n == 1:
        return 1

    # if n is odd, it has no even divisor smaller than n
    if n % 2 == 1:
        return n

    # find the largest number that divides n evenly and is smaller than n
    max_divisor = -1
    for i in range(2, int(n ** 0.5) + 1):
        if is_divisor(i, n):
            max_divisor = max(max_divisor, i)

    return max_divisor
