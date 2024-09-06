```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This behavior is demonstrated in the example below:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The list `['abc', 'array']` is returned because both pass the condition that they start with the prefix `"a"`. 

This function uses list comprehension, a powerful Python feature, to create a new list by filtering strings that satisfy the condition `string.startswith(prefix)`. The `startswith()` method is used to check if a string starts with a specified prefix. 

The script includes type annotations through the `typing` module, specifying that the function `filter_by_prefix` takes a list of `str` and a `prefix` of type `str` and returns a list of `str`. These type annotations can be used with IDEs and tools to provide helpful features such as autocompletion and type checking. 

This function is straightforward and does not require any additional libraries. It is also quite efficient because the `startswith` method uses hashes and bookmarks to find the prefix, which means 0(n) time complexity for each string comparison. 

This solution should help provide an idea of how you can solve the problem and some key points to consider when writing Python functions, especially considering efficiency, best practices, and some common Python idioms.  If you want to refine or extend the function to handle edge cases or improve efficiency some more, let's discuss that further.