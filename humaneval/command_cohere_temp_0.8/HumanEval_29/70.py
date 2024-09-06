```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. 

To achieve this, it uses a list comprehension, iterating over each string in `strings` and generating an inclusive boolean value for whether the current string starts with `prefix`. This boolean value is used to filter the strings accordingly. 

Would you like to generate more examples of test cases to validate this function? Feel free to ask if you'd like more information on the solution or any other aspect of the code.