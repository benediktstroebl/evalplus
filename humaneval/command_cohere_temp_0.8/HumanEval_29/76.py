```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that start with the `prefix`. It uses a list comprehension to iterate through each string in `strings`, and returns the ones that start with the input `prefix`. 

Here's an example of how you can use the function with a sample input:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, it returns the two strings that start with the 'a' prefix which are 'abc' and 'array'. 

This function is reusable and can be easily invoked with different lists of strings and prefixes to filter. 
If you wish to further develop this function or have additional questions, feel free to ask!