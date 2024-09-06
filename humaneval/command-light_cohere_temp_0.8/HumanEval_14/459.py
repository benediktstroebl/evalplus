```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join([x for x in string if x != '']) or [string]
```
This code defines a function called **`all_prefixes`** that takes a string as input and returns a list of all prefixes from shortest to longest of the input string. The function utilizes a list comprehension and filtering to achieve this. 

Let's break down the code and its functionality:
- The function **`all_prefixes`** is defined with one parameter, which is of type **str**. This string parameter represents the input string that we want to generate a list of prefixes from.
- Inside list comprehension is used within the function. It iterates over each characters of the input string (**string**). Then, it checks if each character is not an empty string by using the **`is not ''`** condition. 
If the character is not an empty string, it is included in the resulting list of prefixes.

- If the list comprehension condition is not met for any character, the character is skipped, and the list comprehension stops. The character is then treated as an empty string. This means in the string to be added to the list of prefixes.

- Finally, the function returns the resulting list of prefixes. The function is effectively generating a list of all non-empty strings from the input string, starting from the shortest prefix to the longest prefix.

This code demonstrates a self-contained and concise way of solving the problem of finding all prefixes in a given string.