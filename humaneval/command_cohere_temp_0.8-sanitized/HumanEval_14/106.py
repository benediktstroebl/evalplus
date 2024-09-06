import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    # Find all non-overlapping prefixes and sort them in descending order
    prefixes = sorted(re.findall(r'(.)+', string), key=lambda x: -len(x))
    return prefixes