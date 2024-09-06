

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Use dynamic programming to find the largest divisor
    # The solution is based on the observation that if n is divisible by x, then n is also divisible by x+1, since n = x(x+1)/2
    # This means that if we have found the largest divisor for n, any larger divisor must be greater than the largest divisor by 2
    # We can therefore use a simple linear search to find the largest divisor, by checking the largest divisor for the smallest n
    # that can be represented by the array
    divisors = [2] * (n+1)
    largest_divisor = 2
    for i in range(2, n+1):
        for j in range(i, n+1):
            if divisors[j] % divisors[i] == 0:
                # If j and i are relatively prime, then j cannot be the largest divisor
                break
        else:
            largest_divisor = max(largest_divisor, i)
    return largest_divisor
