
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i = 2
    while i < 100:
        # so i is like this:
        #   2 x 3 x 5 x 7 x 11 x 13 x 17 x 19 x 23 x 29
        # 3, 5, 7, 11, 13, 17, 19, 23, 29 are prime numbers
        # we can see that it is as though there is a pattern
        # 3 times 2, 3 times 3, 3 times 5, 3 times 7, 3 times 11, 3 times 13, 3 times 17, 3 times 19, 3 times 23, etc
        # this is like a repeating pattern
        # so we can see that the number you are looking for is actually made of a pattern
        # that repeats exactly 3 times
        # we can see that when we find a match for 3 times, we know that is is from a pattern 
        # and we can increment i by the pattern and we know that the number we are looking for is not made of a pattern
        if is_triangle_number(a / i) and is_prime(i) and is_prime(a / i):
            i = i + 2
        else:
            i = i + 1
    return a / i == 3

