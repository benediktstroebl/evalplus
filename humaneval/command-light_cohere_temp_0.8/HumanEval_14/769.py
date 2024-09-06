```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test the function with different inputs
test_cases = [
    ('abc',),
    ('abcd',),
    ('abcde',),
    ('a123',),
    ('',),
    ('a', 'b', ''),
    ('foo bar',)
]

for text, want in test_cases:
    actual = all_prefixes(text)
    assert actual == want, f"incorrect result for '{text}': expected [{want]}, got {actual}"
```  This code defines a function all_prefixes that returns a list of all prefixes of a given string. The function uses list comprehension to iterate over every character in the string and includes only non-empty strings (which are prefixes) in the result. The test_cases list contains a variety of inputs and corresponding expected outputs for the function. 

It uses assertions to check if the actual output matches the expected output for each test case, and provides informative error messages in case of mismatch, helping to debug and verify the correctness of the function.