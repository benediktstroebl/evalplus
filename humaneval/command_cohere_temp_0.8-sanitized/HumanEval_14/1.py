import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # find all non-empty prefixes and sort them alphabetically
    return sorted(re.findall(r'^(\w+)', string), key=lambda x: len(x), reverse=True)