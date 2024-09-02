from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    def get_prefixes(string: str) -> List[str]:
        prefixes = []
        for i in range(len(string) + 1):
            prefix = string[:i]
            if not prefix:
                prefixes.append(prefix)
            else:
                prefixes.append(prefix + [string[i]])
        return prefixes

    return get_prefixes(string)