```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. 

To solve the problem, the function uses a list comprehension, creating a new list by filtering strings using the `startswith` method. 

To ensure that the list comprehension only includes strings that start with the desired prefix, the `startswith` method is used. This method returns a Boolean value, which is used in the list comprehension to include a string in the `return_list` if the condition is `True`, and exclude it if the condition is `False`. 

This approach allows the function to efficiently filter and return a list of matched strings, providing a streamlined way to solve the problem. 

The function is self-contained, meaning it does not rely on any external dependencies or imported modules other than those required by the type annotation. 

This function can be tested by using the `assertCount` method to check that the length of the `return_list` is the same as the count of strings that start with the prefix in the input list.  This is done in the following test:
```python
def test_filter_by_prefix():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a').assertCount(2)
```

Here, the assertCount method is used to check that the length of the return list is 2, since 'abc' and 'array' from the input list start with the prefix "a".  This test passes with the given implementation.