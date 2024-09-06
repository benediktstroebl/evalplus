```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This algorithm uses a list comprehension, which is a concise way to create a new list by applying an operation to each item in the existing list. Let's break down the code further:
- The `from typing import List` declaration imports the `List` type from the `typing` module, which allows for explicit type annotation of the function arguments and return value.
- The function `filter_by_substring` takes two arguments: `strings`, which is a list of strings, and `substring`, which is also a string.
- The `return` statement uses a list comprehension to iterate over each string in the `strings` list and checks if the `substring` is present in each string. The implicit iteration over the `strings` list is achieved through the use of the `for string ...` syntax, which is a concise way to create a list iterator. 
- If the substring is found in the string, the string is included in the new list that is returned by the function.

The function is designed to be self-contained and does not rely on any external variables or additional functionality. It efficiently solves the problem of filtering strings containing a given substring and provides a clear and concise implementation that potential users can understand and employ directly in their projects. 

This approach enables the function to be easily reused and integrated into various code bases, facilitating the efficient solution of the problem in different contexts.