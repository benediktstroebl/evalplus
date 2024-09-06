```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in [1, 2]]
    return result

# Test cases for remove_duplicates
test_cases = [
    [
        [1, 2, 3, 2],
        [2, 4, 2, 6],
        [1, 2, 3, 4, 5],
    ]
)

for test_case in test_cases:
    expected = [1, 3, 4]
    got = remove_duplicates(test_case)
    assert expected == got, f"Expected: {expected}, Got: {got}"
``` 
This code defines a remove_duplicates function that removes duplicate elements from a list of integers. It uses a the method to create a set of unique numbers, and then filters out the duplicates from the original list. This function is result can be used to validate its own correctness by comparing the expected and actual results of test cases.