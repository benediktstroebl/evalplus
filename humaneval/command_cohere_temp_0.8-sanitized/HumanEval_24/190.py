def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Nestor division
            if j > i:  # the largest divisor is the numerator
                return i
            else:      # the largest divisor is the denominator
                return j
    else:
        return -1  # error, no divisor found