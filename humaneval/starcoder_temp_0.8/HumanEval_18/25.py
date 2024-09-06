

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if not string or not substring:
        return 0

    if len(string) < len(substring):
        return 0

    def _find(string, index, substring, sub_index):
        if index >= len(string) or sub_index >= len(substring):
            return 0

        if string[index] == substring[sub_index]:
            if sub_index + 1 == len(substring):
                return 1

            return _find(string, index + 1, substring, sub_index + 1) + _find(string, index + 1, substring, sub_index)

        return _find(string, index + 1, substring, sub_index)

    return _find(string, 0, substring, 0)
