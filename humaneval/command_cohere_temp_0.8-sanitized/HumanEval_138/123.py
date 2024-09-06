def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of 4 positive even numbers
    # First, check if the number is less than 4
    if n < 4:
        return False
    # Number greater than 4, check if it's divisible by 2
    elif n % 2 == 0:
        return True
    else:
        return False