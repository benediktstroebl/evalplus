from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    def get_prefixes(string):
        prefixes = []
        for i in range(len(string)):
            prefixes.append(string[0:i+1])
            for j in range(i, len(string)):
                prefixes.append(string[0:j+1] + string[j+1:])
        return prefixes

    return get_prefixes(string)(string)

