

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # You may use the following list of functions to solve this problem
    # str.isalpha(): bool, return True if string is not empty and consist only of letters
    # str.islower(): bool, return True if all characters are lowercase
    # str.upper(): str, return uppercase version of the string
    # str.lower(): str, return lowercase version of the string
    # str.isnumeric(): bool, return True if string consist only of digits
    # str.isdigit(): bool, return True if all characters are digits
    # str.isalnum(): bool, return True if string consist only of letters or digits
    # str.isspace(): bool, return True if string consist of only whitespace characters
    # str.isspace(): bool, return True if string consists of only whitespace characters
    # ord(): ordinal value of given character
    # chr(): character with given ordinal value
    # list.count(): number of occurrences of given element in a list
    # list.sort(): sorts the elements of a list

    lower_string = string.lower()

    if lower_
