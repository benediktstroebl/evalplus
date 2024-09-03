from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join() for i, char in enumerate(string, 1) if char != ' ' and i != 0]