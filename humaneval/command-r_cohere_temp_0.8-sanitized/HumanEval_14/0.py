from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return a list of all prefixes of the input string from shortest to longest.
    """
    prefixes = []
    prefix = ""
    for char in string:
        prefix += char
        prefixes.append(prefix)
    return prefixes[::-1]