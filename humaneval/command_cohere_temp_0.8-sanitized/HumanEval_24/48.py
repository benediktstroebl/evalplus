def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # incumbent
            if j > i:  # to make sure i is not larger than the incumbent
                return i
            if j < i:  # to make sure i is not smaller than the incumbent
                return j
    return n  # return n if no dividers found