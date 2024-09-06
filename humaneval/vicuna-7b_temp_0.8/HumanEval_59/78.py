

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    if n < 2:
        raise ValueError("n must be positive")
    n_list = [n]
    while n_list and n_list[-1] % n_list[-1] == 0:
        n_list.pop()
    if not n_list:
        raise ValueError("n must have at least one prime factor")
    largest = n_list[-1]
    for num in n_list[1:]:
        if num > largest:
            largest = num
    return largest