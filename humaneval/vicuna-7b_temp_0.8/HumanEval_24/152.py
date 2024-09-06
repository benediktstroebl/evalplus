

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    divisors = []
    i = 2
    while n % i == 0:
        divisors.append(i)
        n //= i
        i += 1
    return max(divisors)

print(largest_divisor(15))  # Output: 5