def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i  # return the larger of i or j
    return 1  # if no factors, return 1