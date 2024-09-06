
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # For this problem, we have to check whether we can partition n into exactly 4 equal parts of even number
    # So if n is a multiple of 4, it is possible to partition n into exactly 4 equal parts of even number.
    # Now, if n is not a multiple of 4, we can partition n into 3 equal parts of even number, with the last part
    # being equal to n%4. So n is equal to the sum of exactly 4 even numbers only if n%4 is equal to 0.

    # So for the given n, we have to check whether it is a multiple of 4 and whether n%4 is equal to 0.
    # We can check whether a number is a multiple of 4 by checking whether it is divisible by 4.
    # We can check whether n%4 is equal to 0 by checking whether n%4 is equal to 0.

    # So we check whether n is divisible by 4 and whether n%4 is equal to 0.
    # If both conditions are true, then n is equal to the sum of exactly 4 even numbers.
    
