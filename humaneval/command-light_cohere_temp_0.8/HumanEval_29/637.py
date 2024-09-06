Here is a Python script that solves the problem you have provided:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings that start with that prefix. It uses the string.starting_with to check if each string in the list starts with the given prefix.

The function then passes the test cases provided in the comments, which should return the expected results.

Let's break down the code and explain each part.

- Importing the `typing` module allows us to use type hints in our code. This is used to improve the readability and maintainability of the code.
- The function definition starts with the `def` keyword, which is a Python keyword that defines a function.
- The function name is `filter_by_prefix`, which describes the purpose of the function: it filters strings based on a given prefix.
- Inside function takes two parameters:
  - `List[str]`: This is the first parameter, which is a list of strings. It's a common practice to pass the input to a function.
  - `str`: This represents the prefix string we want to filter.
- The function uses a list comprehension technique to filter the strings in the list. It uses the `x if` statement to check if each element in the list (`x`) starts with the given prefix (`prefix`).
- The `startswith` method is a string method that checks if a string starts with another string. If `x` returns true, then it means that `x` starts with `prefix`.
- If the condition is true, the element `x` is added to the new list that will be returned by the function.

- Finally, the new list that contains only the strings that start with the given prefix is returned.

In summary, the function filters the input list of strings and returns a new list that contains only the strings that start with the specified prefix. The use of the list comprehension and the `startswith` method to achieve this. 

This is a self-contained Python function that solves the problem of filtering strings based on a given prefix.