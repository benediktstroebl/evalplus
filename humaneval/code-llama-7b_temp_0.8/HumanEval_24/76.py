

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # This problem can be solved using a for loop, but I'll attempt to solve it with math
    # We can start with the given number n
    # First, we can set the largest number to be n//2, as no number greater than n//2 can divide n
    largest_number = n // 2
    # We can now keep decreasing the largest number until we have found the largest number
    # Note that we do not need to check numbers greater than n, as they cannot be a divisor
    while largest_number > 1:
        # If n is evenly divisible by the current largest_number, we have found our answer
        if n % largest_number == 0:
            return largest_number
        # If n is not evenly divisible by the current largest_number, we need to try a smaller number
        else:
            largest_number -= 1
    # If we haven't returned by now, it means that n is prime
    return 1

