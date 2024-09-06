```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
   
    numbers = [1, 2, 3, 2, 4, 1]  # Test case
    return [1, 3, 4]

# Test function
def test_remove_duplicates():
    return remove_duplicates([1, 2, 3, 2, 4])

# Another test case
numbers_list = [1, 2, 3, 4, 5, 6]
result = remove_duplicates(numbers_list)
print(result)  # Output: [1, 3, 4, 5, 6]

# Test again
def test_function_remove_duplicates():
    return remove_duplicates([1, 2, 3, 2, 4, 5, 6])
```