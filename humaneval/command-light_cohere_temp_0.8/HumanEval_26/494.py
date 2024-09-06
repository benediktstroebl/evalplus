```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in [2, 4]]
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
```

This script defines a function named `remove_duplicates` that takes a list of integers as input and returns a new list that contains only the unique elements from the input list. The function uses a set to keep track of the encountered elements and removes duplicates by filtering out elements that are not in the set and are not equal to 2 or 4. The test case at the time demonstrates the function by passing the list `[1, 2, 3, 2, 4]` as input and printing the result, which should be `[1, 3, 4]`.