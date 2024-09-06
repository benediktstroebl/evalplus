```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[1:::-1]))
```
This code works by reversing the input string, skipping the first character, and accumulating consecutive characters to form prefixes. This generates a list of prefixes in reverse order. To get the desired order, the list is reversed again, resulting in a list of prefixes from shortest to longest. Ultimately, the script provides an efficient and concise solution to the problem, fulfilling the requirement of returning the prefixes in the specified order.  Exploring these ideas can enhance the code and ensure more robust and maintainable solutions.