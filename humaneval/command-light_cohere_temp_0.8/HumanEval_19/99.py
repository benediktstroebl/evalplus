```python
import typing


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numbers from zero to nine.
    Valid choices are invalid are non-numeric characters.
    Numbers are separated by spaces, in ascending order.
    Return the string with numbers sorted from smallest to largest
    """
    numbers = numbers.split()  #.split()
    Me
    that numbers is a list of strings, we use the input validation to check that the string can be split into a list of numbers. The list of numbers is then sorted in ascending order with spaces as separators. The sorted list is then joined back into a string and returned.