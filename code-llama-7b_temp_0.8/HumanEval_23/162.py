

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """

    # # (1)
    # return 0 if string == '' else 1 + strlen(string[1:])

    # # (2)
    # return len(string)

    # # (3)
    # length = 0
    # for i in string:
    #     length += 1
    # return length

    # # (4)
    # return len(string)

    # # (5)
    # count = 0
    # for ch in string:
    #     count += 1
    # return count

    # # (6)
    # return sum([1 for ch in string])

    # # (7)
    # return sum(1 for ch in string)

    # # (8)
    # count = 0
    # for ch in string:
    #     count += 1
    # return count

    # # (9)
    # return sum(1 for _ in string)

    # (10)
    return sum(ch != '\0' for ch in string)

