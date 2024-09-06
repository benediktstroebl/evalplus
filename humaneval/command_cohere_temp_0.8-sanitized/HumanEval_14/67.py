from typing import List
from itertools import accumulate
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate([string[i:] for i in range(len(string) + 1)]))