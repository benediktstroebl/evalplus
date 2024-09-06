from typing import List
from itertools import accumulate
def all_prefixes(string: str) -> List[str]:
    return list(accumulate([string[::-1], [character for character in string]])[0])