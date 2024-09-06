```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], [4, 5])

def test_function(func: intersperse) -> None:
    actual_result = func(test_data[0], 4)
    expected_result = [5, 9, 7, 11]
    assert actual_result == expected_result, "Test 1 failed"

    actual_result = func(test_data[1], 2)
    expected_result = [7, 13, 11, 9]
    assert actual_result == expected_result, "Test 2 failed"

# Main function call
inverter = intersperse(test_data[0], 4)
print("Inverter result:", inverted_list)
```