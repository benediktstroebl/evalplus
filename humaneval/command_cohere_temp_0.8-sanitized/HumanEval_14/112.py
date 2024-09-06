import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    # find all non-overlapping prefixes and append to list
    for m in re.finditer(r'^(?!.*\1)', string):
        prefixes.append(m.group())
    return prefixes