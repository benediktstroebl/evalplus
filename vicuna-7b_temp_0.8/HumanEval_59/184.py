

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check for special cases
    if n == 1:
        return 2
    elif n == 2:
        return 2
    elif n < 3:
        return 2
    elif n % 2 == 0:
        return 2
    elif n < 5:
        return 3
    # find the largest prime factor
    else:
        low = 5
        high = (int)(log(n, 2) + 1)
        while low <= high:
            mid = (low + high) // 2
            if mid not in [2, 3, 5]:
                high = mid - 1
            elif n % mid == 0:
                low = mid + 1
            else:
                break
        return mid
