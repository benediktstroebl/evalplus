```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This code implements a solution for the problem you described. The function takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the substring. The code uses the specific search function find to efficiently filter the strings that contain the substring.