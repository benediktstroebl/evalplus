```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]

# Unit tests
test_filter_by_prefix = []
test_filter_by_prefix.push("abc". test_filter_by_prefix.push("hello")
 test_filter_by_prefix.push("test")
 test_filter_by_prefix.push("aa") 

def test():
    assert filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]
    assert filter_by_prefix(["def", "test", "hello"], "hello") == ["test"]
    assert filter_by_prefix(["array", "a", "b"], "a") == ["array"]

test()
``` 
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix, and returns a new list containing only the elements that start with the specified prefix. The unit tests section provides some test cases to verify the correctness of the `filter_by_prefix` function.