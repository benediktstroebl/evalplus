
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    elif n == 0:
        return False
    else:
        # check if all elements in array are even
        # sum of 4 even numbers are always even
        numbers = [2, 4, 6, 8]
        even_sum = sum(numbers)
        return even_sum == n

