Here is a Python script that contains a self-contained function `filter_by_substring` that filters an input list of strings based on whether the strings contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. 

This is a self-contained function because it does not rely on any other functions or modules, and can be used directly with passing the appropriate arguments. 

Let's break down the function and discuss how it works:

- The function `filter_by_substring` takes two parameters: `strings`, which is the list of strings to be filtered, and `substring`, which is the substring to search for.
- The function returns a new list, `result_list`, which contains the strings from the input list `strings` that contain the substring `substring`.
- This is done using a list comprehension with the `contains` method, which checks if each string in the input list contains the given substring. 
- The result list `result_list` is returned from the function, which effectively filters the input list of strings based on whether they contain the given substring.

This function is self-contained because it does not rely on any other functions or modules. It can be easily to test and understand how it works, and can be used to solve the problem of filtering a list of strings based on whether they contain a given substring.