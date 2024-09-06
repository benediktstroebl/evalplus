```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. This is achieved using a list comprehension that iterates over each string in `strings` and returns the ones that have a starting prefix that matches the `prefix` parameter. 

To test this function, you can call it with different lists of strings and prefixes and check if the output list contains only the expected strings:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
>>> filter_by_prefix(['xx', 'xy', 'xyz', 'abc'], 'ab')
['abc']
>>> filter_by_prefix(['xxx', 'xyy', 'xyz', 'abcde'], 'abc')
['abcde']
``` 

The above test cases confirm that the `filter_by_prefix` function is working correctly. It is important to note that the function's implementation is tailored to be efficient, allowing it to traverse the list of strings only once, providing the necessary filtering.