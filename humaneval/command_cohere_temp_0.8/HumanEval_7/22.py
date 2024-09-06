```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list. Let's break down the code further:
- The `from typing import List` statement is a type hint, which indicates that the variable `strings` is a list of strings. Type hints are optional in Python, but they can help make code more readable and provide better documentation.
- The function `filter_by_substring` takes two arguments: `strings`, which is the input list of strings, and `substring`, which is the substring to search for.
- The function returns a list of strings containing only those strings from the input list that contain the given substring. This is achieved using a list comprehension, which is the statement `return [s for s in strings if substring in s]`. Here's how it works:
    - `[s for s in strings if substring in s]` creates a new list, where each element `s` is taken from the `strings` list only if the `substring` is found in `s`. 
    - The condition `if substring in s` checks if the `substring` is present in the string `s`. This is a common way to check for a substring in a string in Python. 

Overall, the provided code offers a clear and efficient solution to the problem. It leverages Python's list comprehension for filtering, making it a concise and expressive piece of code. 

This function could be further improved with additional tests, error handling, and comments to make it more robust and transparent. However, the current code already solves the problem and demonstrates the use of list comprehension in Python.