```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix != '' and len(prefix) > 0]

# Test cases
test_suite = {
    'input': ['abc', 'abcd', 'abcde'],
    'expected': ['a', 'ab', 'abc']
}

test_case_one = all_prefixes('abc')
assert test_case_one == test_suite['expected']

test_cases = [
    # Add more test cases here
]

# Run the test suite
test = unittest.TestLoader(). result = test.load(test_cases)
print('Test results:')
print(result.example)
```