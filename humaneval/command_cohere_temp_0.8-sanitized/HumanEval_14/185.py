import re
from typing import List
def all_prefixes(string: str) -> List[str]:
    # Find all non-empty prefixes of the input string and sort them alphabetically
    return sorted(re.findall('^\\S*?(?=' + re.escape(string) + ')', string), key=len)