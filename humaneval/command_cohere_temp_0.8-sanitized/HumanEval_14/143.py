import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # Pattern to extract prefixes of any length
    pattern = f'^{re.escape(string)}'
    # Find all prefixes with regex
    matches = re.findall(pattern, string)
    # Filter to remove empty strings, if any
    prefixes = [i for i in matches if i]
    return prefixes