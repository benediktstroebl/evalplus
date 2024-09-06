from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # TODO: Implement me
    # Hint: We have two numbers x and y such that sqrt(x) and sqrt(y) are not integers.
    # Hint: We can find this as the fraction that has the smallest denominator such that sqrt(x) and sqrt(y) are
    #   integers with the same denominator.
    # Hint: Take the square root of the first number and check that it has a whole number as a fractional part, and
    #   then use the square root of the second number computed based on the fractional part of the square root
    #   of the first number.
    # Hint: Now repeat the above process for the second number, and pick the two that have the smallest denominator.
    # Hint: Once you have found the two closest elements, use the python package fractions to find the ratio that
    #   corresponds to the smallest denominator.
    # Hint: You can create the fraction from two numbers using the constructor
    # https://docs.python.org/3/library/fractions.html
    from fractions import Fraction
    from math import sqrt

    x = Fraction(sqrt(numbers[0]))
    x_numerator = x.numerator
    x_denominator = x.denominator
    x_denominator_if_even = x_denominator if x_denominator % 2 == 0 else x_denominator + 1

    y = Fraction(sqrt(numbers[1]))
    y_numerator = y.numerator
    y_denominator = y.denominator
    y_denominator_if_even = y_denominator if y_denominator % 2 == 0 else y_denominator + 1

    x_over_y = x / y
    x_over_y_numerator = x_over_y.numerator
    x_over_y_denominator = x_over_y.denominator

    if x_over_y_numerator % x_denominator_if_even == 0 and y_numerator % y_denominator_if_even == 0:
        x