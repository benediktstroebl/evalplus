```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function uses the starts-with operator to filter a list of strings and return only those that start with the specified prefix. The function takes in a list of strings and a prefix as input and returns a new list that contains only the strings that start with that prefix. 

We can use the following code to test the function:
```python
def test_filter():
    assert filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]
```
Do you need help with anything else with Python programming?