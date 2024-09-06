def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Find the largest divisor
            if j > i:
                return j  # Return the largest divisor
            elif i == j:
                return i  # Return the largest divisor if there is only one choice
        elif n % i != 0:
            return i  # Return the largest divisor if there are no divisors higher than i
    else:
        return 1  # If no divisor is found, return 1