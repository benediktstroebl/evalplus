from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result = []
    current_len = len(string)
    for prefix in string:
        prefix_len = len(prefix)
        if prefix_len < current_len:
            continue
        result.append(prefix)
        current_len -= prefix_len
        for i in range(1, prefix_len):
            result.append(prefix[0:i] + prefix[i:])
    return result

