from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Write your code here
    if string == "":
        return []
    else:
        short_string = string[:-1]
        long_string = string
        new_prefixes = all_prefixes(short_string)
        new_prefixes.append(long_string)
        return new_prefixes

