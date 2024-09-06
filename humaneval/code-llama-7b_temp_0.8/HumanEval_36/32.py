

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    # Create a list of numbers less than n
    num_list = [x for x in range(n) if x % 11 == 0 or x % 13 == 0]
    # Filter the list of numbers and append them to a new list if the digits of the number have 7
    filter_list = [x for x in num_list if str(x).find("7") > -1]
    return len(filter_list)

