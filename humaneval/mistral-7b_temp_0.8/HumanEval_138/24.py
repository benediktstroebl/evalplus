
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    """
    Start with an example and split it in half
    a = b + c + d
    a = (a - b) + b
    a = (a - b - c) + b + c
    a = (a - b - c - d) + b + c + d

    Try to avoid using modulo. If you are adding numbers modulo 2, you are also subtracting. Subtracting is a bit trickier
    than adding, since if you try to subtract a larger number from a smaller number, you will have a negative result.
    Since 2 is smaller than 1, we don't need to worry about negative numbers.

    Example
    n = 8
    n = 8 - 4 - 2 - 2
    n = 0 - 4 - 2 - 2
    n = 4 + 4 + 2 + 2
    """

    if n % 2 != 0:
        return False

    n //= 2

    a = b = c = d = 0

    while n >= 4:
