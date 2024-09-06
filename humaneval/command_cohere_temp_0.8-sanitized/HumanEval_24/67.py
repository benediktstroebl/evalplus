def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # noon-negative quotient
            if j > i:  # i is the largest divisor
                return i
            elif j == i and i > 0:  # this case catches oddities like 9 / 3 = 3
                return i
    return 1  # we've checked all possibilities; nothing divides n perfectly