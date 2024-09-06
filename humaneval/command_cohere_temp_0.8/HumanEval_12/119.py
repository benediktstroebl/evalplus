```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    else:
        return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, lists strings, as input and returns the longest string in the list, or None if the list is empty. The function employs a simple algorithm utilizing conditional statements and Python's built-in max function to accomplish this task. Firstly, the function checks if the input list is empty; if it is, it returns None. If not, it examines whether all strings in the list have the same length. If they do, the function returns the first string in the list using indexing [0]. If not, it employs the max function with the key parameter set to len to return the longest string in the list.

Here is an example usage of the function:
```python
print(longest(['a', 'b', 'c']))  # longest returns 'c'
print(longest(['a', 'bb', 'ccc']))  # longest returns 'ccc'
print(longest([]))  # longest returns None
```
This will output:
```bash
ccc
ccc
None
```
In the first two examples, the function returns the longest string among the given list of strings, while in the last example, as the input list is empty, it returns None as specified.