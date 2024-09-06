```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `return_list`, which contains only the strings from the input list that contain the given substring. 

To solve this problem, the function uses a list comprehension, creating a new list and filtering its elements based on the condition of containing the specified substring. 

Here's an example of how you can use the function to filter a list of strings containing the substring "a":
```python
>>> filter_by_substring(
    ['abc', 'bacd', 'cde', 'array'], 
    'a'
)
['abc', 'bacd', 'array']
``` 

The function returns the list of strings that contain the given substring, which in this case are `abc`, `bacd`, and `array`. 

This approach works efficiently even for large input lists and is a straightforward way to solve this problem.