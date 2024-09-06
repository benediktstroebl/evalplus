import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    # Find all non-empty prefixes of the input string and sort them by length
    # from shortest to longest
    prefixes = sorted(re.findall(r'^(\w+)', string), key=len, reverse=True)
    return prefixes