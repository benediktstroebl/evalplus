from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    current_string = string
    for prefix in get_prefixes(current_string):
        current_string = current_string[len(prefix):]
        result.append(prefix)
    return result
