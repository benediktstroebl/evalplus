from typing import List
import re
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if re.find(prefix, string)]