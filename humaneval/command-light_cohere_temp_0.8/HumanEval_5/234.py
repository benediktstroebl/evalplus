```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter]

# Test the function with different inputs and verify the output
numbers_list = [1, 2, 3]
result_list = intersperse(numbers_list, 4)
assert len(result_list) == 6
assert all(isinstance(result_list[i], int))  # Verify each element is an integer
assert all(result_list[i+1] == result_list[i]+2)  # Verify the functionality

# Example 2: Split numbers with spaces
numbers_list = ['1', '23', '45']
result_list = intersperse(numbers_list, ' ')
assert len(result_list) == 3
assert result_list[0] == '1 '  # Verify the output

# Example 3: Split integers with dots
numbers_list = [123, 45, 67]
result_list = intersperse(numbers_list, '.')
assert len(result_list) == 3
assert all(result_list[i].isdigit())  # Verify each element is an integer

# Example 4: Split complex string
numbers_list = "1:23 45:67"
result_list = intersperse(numbers_list, ':')
assert len(result_list) == 3
assert all(result_list[i].isdigit())  # Verify each element is a valid integer
```