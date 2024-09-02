from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Base case: return empty list
    if string == "":
        return []

    # Recursive case: call your self with the substring
    return [string[0]] + all_prefixes(string[1:])

