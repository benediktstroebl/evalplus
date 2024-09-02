
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Write a function to check if a number is even
    def is_even(x):
        return x % 2 == 0

    # Write a function to check if a number is positive
    def is_positive(x):
        return x > 0

    # Write a function to check if a number is even and positive
    def is_positive_even(x):
        return is_even(x) and is_positive(x)

    # Write a function to check if a number can be written as the sum of 4 positive even numbers
    def can_be_summed_to_4_even(x):
        return is_positive_even(x) and is_positive_even(x - 2) and is_positive_even(x - 4) and is_positive_even(x - 6)

    # Test the function with some examples
    for i in range(1, 10):
        if is_equal_to_sum_even(i):
            print(i, "is equal to the sum of exactly 4 positive even numbers")
