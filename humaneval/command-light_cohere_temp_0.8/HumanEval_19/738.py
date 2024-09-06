```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(num) for num in numbers.
    return ' '.join(sorted(numbers))

# Unit tests
def test_sort_numbers():
    test_cases = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for test_case, expected_output in test_cases.
    actual_output = sort_numbers(test_case)
    assert actual_output == expected_output
```