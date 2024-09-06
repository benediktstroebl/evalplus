```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)

# Test the remove_duplicates function
numbers = [1, 2, 3, 2, 4, 3, 2, 1]
result = remove_duplicates(numbers)
print(result)

# Test the function with set input
numbers2 = set([1, 2, 3, 4, 5])
result2 = remove_duplicates(numbers2)
print(result2)
```

The code defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The test cases pass the dry and the expected output is printed, which shows that the function removes duplicate elements correctly.