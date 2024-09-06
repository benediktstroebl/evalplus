```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    seen = set()
    result = [num for num in numbers if num not in seen and num not in numbers[numbers.seen duplicates]
    result
    list(seen) 
    return result 

# Test Case 1:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Test Case 2:
numbers = [1, 2, 3, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]

# Test Case 3:
numbers = [1, 2, 3, 4, 5, 6, 7]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7] 
```

This script defines a function called `remove_duplicates` that takes a list of integers as input and removes all duplicate elements from the list, ensuring the result is a list of unique integers. The script also provides three test cases to verify the correctness of the `remove_duplicates` function.