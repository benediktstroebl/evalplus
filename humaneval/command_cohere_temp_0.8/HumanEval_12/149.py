```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the code above that takes a list of strings, initials Optional[str] and returns the longest string in the list. If the list is empty, it returns None. If there's only one string in the list, it returns the unique string from the list. If there are multiple strings of the same length, it returns the first one using the max function to select the first string among the duplicates.

Here's an example of how you can use the longest function explicitly with the argument [''], which returns None since an empty list is passed:
```python
print(longest([]))
```
This will output None since the longest string in an empty list is None.

Here's another example that shows the longest function in use, this time with the argument ['a', 'b', 'c'], which returns 'a' since it is the longest string in the list:
```python
print(longest(['a', 'b', 'c']))
```
This will output: ```anme: 'a'```

Lastly, for the input ['a', 'bb', 'ccc'], the function will return ccc, since it's the longest string and the key parameter in the max function is set to len, making the comparison based on string length. 

These examples show how the function operates with different inputs, highlighting its capability to handle various scenarios and return the longest string from the list.  If you wish, you can use this code snippit in your problem specification document. Feel free to ask if you would like any further assistance!