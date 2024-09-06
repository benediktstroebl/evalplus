def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # numerator
            k = i     # denominator
            m = j // k  # i is the largest divisor if j is the largest numerator and k is the largest denominator
            if m == i:
                return i
        else:
            continue
    return -1