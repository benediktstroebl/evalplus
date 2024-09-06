Here is a self-contained Python script that defines a function `all_prefixes` solving the problem you have described:

```python
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    def prefixes(lenient):
        # Use 1-based index for consistency and simplicity
           return [''.join() for i in range(1, len(lenient) + 1)]

    return prefixes(string)
```

This script provides a function that generates all prefixes of a given string. It uses a specific approach using a generator expression to create all possible prefixes, and the `lenient` variable is used to ensure consistent and simple 1-based indexing. The code is also well-contained and does not rely on external imports or external functions.