

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # TODO: This is your job

    if string == "" or substring == "":
        return 0

    else:
        counter = 0
        position = 0
        while string[position] != "":
            if string[position:position+len(substring)] == substring:
                counter += 1
            position += 1
        return counter

