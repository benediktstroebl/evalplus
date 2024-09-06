from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # return [string[i:] for i in range(len(string)+1)]
    # return list(string)
    # return [string[:i+1] for i in range(len(string))]
    # return [string[:i] for i in range(len(string)+1)]
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result

