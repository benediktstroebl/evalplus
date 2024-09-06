```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # tests = ['a', 'ab', 'ccc', 'abc', '123']
    # tests = [('abc', ['abc']), ('ab', ['ab']), ('aa', ['a'])]
    # assert all(tests), f"Failed: {tests}"
    # print(tests)
    # print(str.join(tests))
    return tests
```
The above code defines a function called `all_prefixes` that takes a string as input and returns a list of all prefixes from the shortest to the longest characters in the input string.