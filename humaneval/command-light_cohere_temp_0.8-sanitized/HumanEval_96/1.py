def count_up_to(n):
    """Return an array of prime numbers less than or equal to n."""
    if n <= 1:
        return []
    elif n <= 3:
        return [2]
    elif n % 2 == 0 or n % 3 == 0:
        return [2, 3]
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return [i, i + 2]
        i += 6
    return []