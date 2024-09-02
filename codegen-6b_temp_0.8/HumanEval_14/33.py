from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    shortest_string = string
    longest_string = string
    list_of_prefixes = []

    while len(shortest_string) > 0:
        list_of_prefixes.append(shortest_string)
        shortest_string = shortest_string[:-1]

    list_of_prefixes.reverse()

    return list_of_prefixes

