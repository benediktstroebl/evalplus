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
This Python script defines a function called longest in the code above that takes a list of strings, called strings, as input, and returns the longest string in the list. If the input list is empty, the function returns None. If there's only one string in the list, the function returns the unique string, regardless of its length. Otherwise, the function returns the longest string in the list using the max function, with the length of each string as the key for grouping. 
The function utilizes the max function to compute the longest string within the list of strings. The key parameter of the max function is set to the length of each string, enabling grouping and sorting by length.

Here is an example of how you can use the function:
```python
print(longest(['a', 'bb', 'ccc']))
```
This will output:
ccc

The function handles an empty list and lists with one or more strings and returns the longest string accordingly. You can use the function to solve the problem described in the markdown code block provided.