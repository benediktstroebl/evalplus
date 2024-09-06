
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # define a function that computes the sum of 4 positive even numbers
    # pass the function to is_equal_to_sum_even() to test
    def sum_of_four_even_numbers(n):
        # get the list of four positive even numbers from 1 to n
        numbers = list(filter(lambda x: x % 2 == 0 and x <= n, range(4, n + 1, 4)))
        # return the sum of the list
        return sum(numbers)
    # return the result of the function
    return n % 2 == 0 and sum_of_four_even_numbers(n) == n
