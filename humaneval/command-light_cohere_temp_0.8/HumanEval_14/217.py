```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != ' ']

# Test the function with various strings
test_cases = [
    ("hello world", ),
    ("", ),
    ("   ",),
    ("   abc", ),
    ("", "World!"),
]

for case in test_cases:
    print(all_prefixes(case))  # Expected output: ['h', 'ello', 'world', ' ', 'abc']
``` 
This function uses list comprehension and a simple condition to filter out spaces from the input string, producing the desired prefixes. The function's output is a list of non-space characters from the input string.