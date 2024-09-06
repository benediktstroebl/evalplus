def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            j = n // i  # Anchor the loop to hunt for the largest divisor
            if j > i:  # Update i if j is larger to hunt for a larger divisor
                i = j
            if i > largest_divisor.result:
                largest_divisor.result = i  # Keep track of the largest divisor encountered
    return largest_divisor.result