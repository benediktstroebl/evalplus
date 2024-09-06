```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string if i != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    '   ',
    'a',
    'aa',
    '123abc'
]

results = {}
for test_case in test_cases:
    print(test_case)
    prefixes = all_prefixes(test_case)
    results[test_case] = prefixes

print(results)
``` 
This Python script defines a function called `all_prefixes` that returns a list of all prefixes in a given string. The script then provides a list of test cases, and loops through them, passing each string to the `all_prefixes` function to get the corresponding list of prefixes. Finally, the script prints out results, which are the lists of prefixes for each test case.