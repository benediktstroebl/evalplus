```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.sorted() if prefix != '' and not prefix.
    """
``` 
This function uses the sorted() method with a lambda function to generate all prefixes from the shortest to the longest of the input string. 

Please note that this solution is already self-contained and does not require any additional imports.