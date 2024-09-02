

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    substring_len = len(substring)
    count = 0
    # while True:
    #     try:
    #         index = string.index(substring, 0)
    #         count += 1
    #         string = string[index + 1:]
    #     except ValueError:
    #         break
    #     # if count >= substring_len:
    #     #     break
    #     # count += 1
    #     # index += substring_len
    #     # if index >= len(string):
    #     #     break
    # return count

    return string.count(substring)

