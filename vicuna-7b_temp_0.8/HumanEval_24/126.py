

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    def divisors(x):
        if x == 0:
            return []
        else:
            return [x % y for y in range(1, int(x**0.5) + 1)]
    
    def largest_divisor_helper(x):
        if x > n:
            return -1
        if n % x == 0:
            return x
        for y in divisors(n - x):
            if y > largest_divisor_helper(y):
                return y
        return largest_divisor_helper(1) + 1
    return largest_divisor_helper(n)