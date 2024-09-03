from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if c.isalpha() else '_' for c in string]