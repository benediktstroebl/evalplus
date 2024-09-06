```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]


# Test cases
strings = ["abc", "bcd", "cde", "array", "hello", "world"]
prefix = "a"

print("Test 1 result:", filter_by_prefix(strings, prefix))

print("Test 2 result:", filter_by_prefix([u'abc' for u in strings], prefix))

print("Test 3 result:", filter_by_prefix(["123", "abc"], prefix))
```  This script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. 
The function uses the list comprehension and the `startswith` method to filter the strings. 

The function is then tested with three different test cases.