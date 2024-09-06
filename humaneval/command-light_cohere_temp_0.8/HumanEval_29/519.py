```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [s for s in strings if s.startswith(prefix)]


# Test case 1: Filter words starting with 'a'
test_case_1 = [
    'abc',
    'bcd',
    'cde',
    'array',
    'aardvarks'
]
filtered_case_1 = filter_by_prefix(test_case_1, 'a')
assert filtered_case_1 == ['abc', 'array']


# Test case 2: Filter words starting with 'geeks'
test_case_2 = ['geeks', 'code', 'test', 'gears', 'soph']
filtered_case_2 = filter_by_prefix(test_case_2, 'geeks')
assert filtered_case_2 == ['geeks', 'code', 'test']


# Test case 3: Filter words starting with multiple prefixes
test_case_3 = ['one', 'a', 'data', 'is', '1', 'abc']
filtered_case_3 = filter_by_prefix(test_case_3, 'a')
assert filtered_case_3 == ['a', '1', 'abc']


# Test case 4: Filter words not starting with any prefix
test_case_4 = ['hash', 'date', 'coded', 'active']
filtered_case_4 = filter_by_prefix(test_case_4, '')
assert filtered_case_4 == []


# Print the results of the above tests
print("Test case 1: " + filtered_case_1)
print("Test case 2: " + filtered_case_2)
print("Test case 3: " + filtered_case_3)
print("Test case 4: " + filtered_case_4)")
 ```
This Python script defines a function called `filter_by_prefix` that filters an input list of strings based on a given prefix. The script includes a self-contained test cases, which demonstrate how the `filter_by_prefix` function works and validates its behavior with different inputs. 
After the tests, the script prints the results to the console.