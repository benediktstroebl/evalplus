

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    max_divisor = max(divisors)
    return max_divisor

if __name__ == '__main__':
    # test the function
    assert largest_divisor(15) == 5
    assert largest_divisor(20) == 2
    assert largest_divisor(30) == 3