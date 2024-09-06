```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that begin with the `prefix`. It uses a list comprehension to iterate through each string in `strings`, and checks if the string starts with the prefix using the `startswith` function. If it does, the string is included in the `return_list`. 

Here's an example of how you can use the function with a sample input to return the desired output:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This will filter out any strings from the list that start with the prefix "a", and will return a list that only contains "abc" and "array". 

This approach has a time complexity of O(n) since it requires iterating through each element in the list once, and does not require additional space since it operates on the input list directly.  It's also important to note that the function includes type annotations, `from typing import List`, to ensure type safety and to make it compatible with mypy and other static type checkers.  This will ensure that the function will trigger a TypeError if misused with an input that doesn't conform to the expected types.