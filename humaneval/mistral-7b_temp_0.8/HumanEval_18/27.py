

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    substring_length = len(substring)
    # print(substring_length)
    # print(len(string))

    # Increasing the counter when the substring is found
    # Decreasing the counter when the substring is over
    counter = 0
    for i in range(len(string) - substring_length + 1):
        if string[i: i + substring_length] == substring:
            counter += 1
        else:
            counter -= 1

    return counter

