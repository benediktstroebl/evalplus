```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that contain `substring` to the new list.

The function is designed to be self-contained, meaning it doesn't rely on external variables or additional logic outside of what's provided in the function signature. You can use it to solve the problem as stated, and it can easily be copied and pasted into your codebase or shared separately. 

To use this function, you can provide your list of strings and the substring you want to filter by as arguments, like this:
```python
input_strings = ['abc', 'bacd', 'cde', 'array']
input_substring = 'a'

result = filter_by_substring(input_strings, input_substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This will return a list containing only the strings from the `input_strings` list that contain the `input_substring `'a'` in this example.