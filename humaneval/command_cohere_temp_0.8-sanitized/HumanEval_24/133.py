def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # smallest number with same divisors as i
            if j < i:
                return i
            elif j > i:
                return j
    return 1