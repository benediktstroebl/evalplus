

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Starting from the number itself, we can check if the number divides the original number evenly,
    # If it does, we found our answer. If it doesn't, we go to the next number and repeat the process,
    # until we find our answer
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

