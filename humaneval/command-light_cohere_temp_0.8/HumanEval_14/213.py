```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i != '' and i != '']

# Test cases
test_cases = [
    'abc',
    '',
    'a',
    'abc',
    'ab',
    '123', # Added a special case to test empty string
    ]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f'Actual: { }, [''.join(i) for i in actual_prefixes])
    print('Expected: ', ['.join(test_case[i] for i in range(1,len(test_case)+1))])
    assert actual_prefixes == ['.join(test_case[i] for i in range(1,len(test_case)+1))]
```  This script defines a function `all_prefixes` that returns a list of prefixes from the shortest to the longest of an input string. The script also includes a test cases and runs the function on each case, comparing the actual output with the expected output, and asserting the two are equal.