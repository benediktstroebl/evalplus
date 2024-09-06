```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function utilizes the `dropwhile` function from the `itertools` module to eliminate elements from the start of the string up until it reaches an empty string. The reversed version of this list is then returned, ensuring that the prefixes are arranged in the desired order of shortest to longest.

To activate this module, simply run `from itertools import dropwhile` at the beginning of your script. 
This approach allows for an efficient and concise way to solve the problem, making it a useful tool for solving similar challenges in the future.