```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the original list that begin with the provided prefix. It uses a list comprehension to iterate through each string in `strings` and checks if it starts with the specified `prefix`. If it does, the string is included in the `return_list`. 

Here's an example of using the function with a sample input and an example of its usage:
```python
sample_input = ['abc', 'bcd', 'cde', 'array']
sample_prefix = 'a'

expected_result = ['abc', 'array']

result = filter_by_prefix(sample_input, sample_prefix)

print(result)  # Expected output: ['abc', 'array']
```

This would create an input list, `sample_input`, and a prefix, `sample_prefix`, and then check whether the resulting output, `result`, is equal to the expected output, `expected_result`.