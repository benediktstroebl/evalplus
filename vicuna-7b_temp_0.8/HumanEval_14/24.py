from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # base case
    if len(string) == 1:
        return [string]

    # split string into pairs of characters
    pairs = [(string[i], string[i + 1]) for i in range(0, len(string), 2)]

    # remove duplicates
    pairs = list(set(pairs))

    # create list of prefixes
    prefixes = [p[0] for p in pairs]

    # append rest of string to prefixes
    prefixes += [p[1] for p in pairs]

    # sort prefixes
    prefixes.sort()

    # return prefixes
    return prefixes

