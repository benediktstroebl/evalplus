from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Your code here
    if string == "":
        return []
    else:
        all_prefixes = []
        for x in range(0, len(string) + 1):
            all_prefixes.append(string[0:x])
        return all_prefixes

