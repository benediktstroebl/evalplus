Here's the self-contained Python script that includes the function `filter_by_prefix` and its corresponding tests:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    :return all strings that start with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]


# Test case 1: filter strings that start with 'a'
test_cases = [
    ['abc', 'a', 'array'],
    ['cba', 'ab'],
    ['b', 'aa'],
    ['a', '100', 'b']
]

test_filter_by_prefix = filter_by_prefix(test_cases, 'a')
print(test_filter_by_prefix)

# Test case 2: filter empty list
test_empty_list = filter_by_prefix([], 'a')
print(test_empty_list)

# Test case 3: filter strings that start with 'ab'
test_cases_2 = [
    ['ab', 'cd', 'ab'],
    ['abcde', 'ab'],
    ['ba', 'a', 'bb']
]

test_filter_by_prefix_2 = filter_by_prefix(test_cases_2, 'ab')
print(test_filter_by_prefix_2)
``` 
This version is a self-contained Python script that contains the function `filter_by_prefix` and its corresponding tests.  It above, we have provided three test cases to verify the correctness of the function.