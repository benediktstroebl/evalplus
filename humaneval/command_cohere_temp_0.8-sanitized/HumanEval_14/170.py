import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    # Get all prefixes with the regex expression
    prefixes = re.findall(r"^(.*)\1*", string)
    # Sort them properly
    return sorted(prefixes, key=lambda x: (len(x), x))