from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    string = str(string)
    prefixes = [string]
    for c in string:
        if c not in string:
            for i in range(1, len(prefixes)):
                prefix = ''.join(prefixes[:i+1])
                if prefix + c in string:
                    prefixes = prefix + [c] + prefixes[i:]
                    break
    return prefixes