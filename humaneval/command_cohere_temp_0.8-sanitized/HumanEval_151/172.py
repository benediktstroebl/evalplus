def double_the_difference(numbers):
    """
    Sum of squares of odd numbers in the list that are integers, ignoring negatives.

    :param numbers: List of numbers.
    :return: Sum of squares of odd integers.
    """
    odd_integers = [num for num in numbers if num % 2 != 0 and num >= 0 and isinstance(num, int)]
    return sum(num ** 2 for num in odd_integers)