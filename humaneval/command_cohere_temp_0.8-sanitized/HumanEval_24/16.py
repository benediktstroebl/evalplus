def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # denominator
            k = i     # numerator
            # the largest divisor is the last divisor
            if j > k:
                return j
            elif j == k:
                return k
    return 1  # return 1 if no number can divide the given number n