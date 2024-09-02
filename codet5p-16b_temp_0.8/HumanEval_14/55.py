from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    def all_prefixes_aux(string, prefixes, index):
        if index == len(string):
            return prefixes

        prefixes.append(string[:index])
        all_prefixes_aux(string, prefixes, index + 1)
        return prefixes

    return all_prefixes_aux(string, [], 0)
