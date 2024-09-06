```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings `strings` and a substring `substring` as input, and returns a new list containing only the strings from the input list that contain the given substring. This function solves the problem using Python's list comprehension, filtering strings that contain the provided substring. 

To validate the functionality of this function, you can use the following tests:
```python
def test_filter_by_substring():
    # Test case from the problem statement
    assert filter_by_substring(
        ['abc', 'bacd', 'cde', 'array'], 'a'
    ) == ['abc', 'bacd', 'array']

    # Edge case where substring is present only once
    assert filter_by_substring(
        ['ab', 'bc', 'cd', 'de', 'ad'], 'ad'
    ) == ['ad', 'bc']

    # Empty input list
    assert filter_by_substring([], 'a') == []

    # Single element list
    assert filter_by_substring(['abc'], 'a') == ['abc']

    # Substring is the whole string
    assert filter_by_substring(['abc'], 'abc') == ['abc']

    # Complex input
    assert filter_by_substring(
        ['hello', 'world', 'abc', 'bcd', 'pqrsw', 'bcde'], 'bc'
    ) == ['abc', 'bcd', 'bcde']
``` 

These tests cover different scenarios of input and edge cases to ensure the function works correctly. 

The code follows the best practices in Python because it's concise, readable, and does not have any potential issues that require attention. 
However, if your goal is to optimize for performance under special circumstances, the code can be optimized further:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for s in strings:
        if substring in s:
            result.append(s)
    return result
```

This version of the code uses a for loop to iterate through each string in the list and directly adds the matching strings to the `result` list. Contrary to the previous version that uses list comprehension, this version runs in linear time instead of constant time for each match. The trade-off is that this code is slightly longer and more readable, which is beneficial if you want to understand the functionality instantly. 

Please note that unless you are dealing with a large dataset or a situation where micro optimizations are necessary, the difference in performance between the two solutions will be negligible and hardly noticeable.