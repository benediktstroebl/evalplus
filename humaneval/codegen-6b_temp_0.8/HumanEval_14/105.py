from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    output = []
    for index, char in enumerate(string):
        output.append(char)
        if index == len(string) - 1:
            break
        output.append(string[0:index + 1])
    return output

