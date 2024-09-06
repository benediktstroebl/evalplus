import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    # Find all non-overlapping prefixes and sort them in reverse order to get prefixes in ascending order of length
    prefixes = [p for p in re.findall(r'(.*?)(?=\b)', string)]
    prefixes.sort(key=lambda x: (-len(x), x), reverse=True)
    return prefixes