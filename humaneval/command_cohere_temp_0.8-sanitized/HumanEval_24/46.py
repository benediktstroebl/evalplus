def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # banker's rule
            if j > i:
                return j
            elif i == j == n // i:
                return i
    return 1