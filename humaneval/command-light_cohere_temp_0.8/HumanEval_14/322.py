```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.py.finditer(r'\., string) for r in range(len(string)) if prefix != '' and r > 0]

# Test case for the function
test_case = "abc"
result = all_prefixes(test_case)
print(result)

# Test case with empty string
empty_string = ""
result = all_prefixes(empty_string)
print(result)

# Test case with only one character
single_char = 'x'
result = all_prefixes(single_char)
print(result)
``` 
This script provides a function that takes a string as input and returns a list of its prefixes. The script also includes several test cases to cover different scenarios, passing them to the function and printing the results.