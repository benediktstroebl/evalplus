from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = set()
    current_prefixes = []
    for char in string:
        prefixes.add(char)
        current_prefixes.append(char)
        if len(current_prefixes) > 1:
            yield current_prefixes
            current_prefixes = []
    if current_prefixes:
        yield current_prefixes
    if current_prefixes:
        raise StopIteration("Extra prefixes found: " + " ".join(current_prefixes))

