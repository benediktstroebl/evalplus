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
This Python script defines a function called longest in the code above that takes a list of strings, trims it to remove any duplicates, and then returns the longest string in the list if there is only one unique string in the list, it returns the first string in the list, and if the list is empty, it returns None. 

Here is an example of how you can call this function:
```python
print(longest(['a', 'bb', 'ccc']))  # Outputs: ccc
print(longest(['a', 'b', 'c', 'a']))  # Outputs: a
print(longest([]))  # Outputs: None
```
We print the output of the longest function using the print() function. In the first example, the output would be ccc because it is the longest string in the list. In the second example, the output would be a because there are two strings with the same length, and the function returns the first one. Finally, the last example would print None because the list is empty. 

This function is straightforward to use and understand, and it efficiently solves the problem it is designed to solve.