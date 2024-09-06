```python
from typing import List
def concatenate(strings: List[str]): 
    """ Concatenate list of strings into a single string """
    return ''.join(strings)
# Unit tests for concatenate function
test_concatenate = [
    ['Should return empty string when empty input'],
    ['a', 'bc'],
    ['abc']
]

def test_function(test_case): 
    actual_result = concatenate(test_case)
    expected_result = test_case[1] 
    assert actual_result == expected_result, f"Test {test_case[0]} failed"

if __name__ == "__main__":
    test_concatenate = test_case()
    test_function(test_concatenate)
```