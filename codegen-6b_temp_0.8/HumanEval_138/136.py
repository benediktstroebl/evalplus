
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    if n < 4:
        return False
    # find all even nums
    evens = [x for x in range(2, n + 1, 2)]

    # Find the sum of all even numbers
    sum_of_evens = sum(evens)

    if sum_of_evens == n or n - sum_of_evens == 4:
        return True
    else:
        return False

