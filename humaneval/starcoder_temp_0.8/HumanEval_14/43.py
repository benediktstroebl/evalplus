from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = list(string)
    output = []
    while string:
        output.append(''.join(string))
        string.pop()
    return output
