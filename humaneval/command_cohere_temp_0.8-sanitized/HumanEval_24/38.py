def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # largest divisor
            if j < i:
                return j  # return the largest divisor if it's less than n
    return 1  # return 1 if no number divides n fully