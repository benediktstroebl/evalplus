
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # ...
    # Your code here
    a = [2, 4, 6, 8]
    b = 0
    for i in range(0,4):
        b = b + a[i]
    if (n == b):
        return True
    else:
        return False

