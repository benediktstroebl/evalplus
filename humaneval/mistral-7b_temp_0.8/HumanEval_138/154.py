
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    def sum_even(n):
        """Checks if a number can be written as the sum of 4 positive even numbers
        :param n: The number to check
        :return: True if the number can be written as the sum of 4 positive even numbers, False otherwise.
        """
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                if i % 2 == 0:
                    return True
        return False

    return sum_even(n)

