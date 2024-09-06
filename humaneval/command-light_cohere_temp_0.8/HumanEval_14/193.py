Here's the self-contained Python script with a function that returns a list of all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i] for i in range(len(string) - 1)] + string.test_case = ["ab", "bc", "cba", "cbb", "ccc"]
    for t in test_case:
        assert all_prefixes(t) == [t[0], t[1], t[2], t[3]]
    return all_prefixes('abc')
```
This function uses Python's built-in list comprehension to generate all possible prefixes of the input string, and the range(len(string) - 1) to generate all possible lengths of prefixes starting from the empty string up to the given length. The function then adds the string itself to get the full string as a possible prefix.