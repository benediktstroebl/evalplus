def double_the_difference(lst):
    """
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    """
    odd_integers = [num for num in lst if num > 0 and isinstance(num, int) and num % 2 != 0]
    return sum(num ** 2 for num in odd_integers)