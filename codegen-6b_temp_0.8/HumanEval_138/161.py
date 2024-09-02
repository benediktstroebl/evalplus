
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return sum(2*n for n in range(1, int(n**0.5)+1, 2) if n % 4 == 0) == n

"""
Task 4 

6-10 = (6 + 8 + 10) = 26 

Write a function that returns True if the given positive integer is a perfect square and False otherwise.
Note: all perfect squares are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, and 13.
"""