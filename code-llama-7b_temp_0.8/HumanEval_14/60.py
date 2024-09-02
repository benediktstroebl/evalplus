from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Here we want to stop on the index before the end of the string, because we
    # want to return all prefixes, not just prefixes up to the first letter.
    return [string[:i] for i in range(len(string))]

