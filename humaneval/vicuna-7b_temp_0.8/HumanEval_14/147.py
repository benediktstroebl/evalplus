from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if len(string) == 0:
        return []

    prefixes = []
    current_prefix = string[:1]
    for i in range(1, len(string)):
        if string[i] == '1':
            current_prefix = current_prefix * 10 + string[i]
        elif string[i] == '0':
            current_prefix = current_prefix * 10 + (string[i-1] + string[i])
        else:
            prefixes.append(current_prefix)
            current_prefix = string[i]

    prefixes.append(current_prefix)

    return prefixes

