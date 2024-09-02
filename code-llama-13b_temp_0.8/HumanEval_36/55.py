

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    # make list to check
    list = []
    for i in range(1, n):
        list.append(i)

    # remove numbers that are not divisible by 11 or 13
    for i in list:
        if not (i % 11 or i % 13):
            list.remove(i)

    # count the number of times 7 appears in the list
    count = 0
    for i in list:
        if str(i).__contains__('7'):
            count = count + 1

    return count

