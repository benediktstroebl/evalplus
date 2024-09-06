from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # MUTATION: []
    result = []
    for i in range(len(string) + 1):
        # COMMENT: slice of empty string is ''
        result.append(string[:i])  # CONCATENATION
    return result

