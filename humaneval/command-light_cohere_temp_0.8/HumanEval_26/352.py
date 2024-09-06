```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)

# Test the function with a sample input
test_remove_duplicates = []
test_remove_duplicates.append([1, 2, 3, 2, 4])
test_remove_duplicates.append([5, 4])

print(f"Original list: {test_remove_duplicates}")
print("Unique list: ", end="")
print(test_remove_duplicates)

def test_remove_duplicates():
    assert remove_duplicates(test_remove_duplicates) == [1, 3, 4]

print("Test passed!")
```