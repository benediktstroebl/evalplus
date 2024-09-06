```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The resulting list is then typed as `List[str]` to avoid any confusion that may arise from the use of the return type `List` without a specific subtype. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This tests the example pointed out in the problem description, and the expected outcome is returned. 

Furthermore, here is another example to test a different use case of the function:
```python
>>> filter_by_prefix(['lecture1', 'lecture2', 'exercise1', 'exercise 2'], 'lecture')
['lecture1', 'lecture2']
```
This tests the function with a new prefix and a new list of strings to check whether the function filters out the strings accordingly. 

If you would like to implement the function with a different approach, I am happy to provide other examples and guidance to ensure the solution is also correct. Please let me know if you would like to iterate on the solution further.