def is_equal_to_sum_even(n):
    # Check whether the given number can be expressed as the sum of 4 even positive numbers
    # By factoring the number into 2*x where x is an odd number
    if n % 2 == 0: 
        x = n // 2
        if x % 2 == 0:
            return True
    return False