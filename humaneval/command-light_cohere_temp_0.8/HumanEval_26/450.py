```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    result = []
    seen = set()
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
# Further, we can add more tests to validate the function.

# Test 1:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output should be [1, 3, 4]

# Test 2:
numbers = [5, 5, 5, 6, 6]
result = remove_duplicates(numbers)
print(result)  # Output should be [5, 6]

# Test 3:
numbers = [1, 2, 3, 4, 5, 6, 6]
result = remove_duplicates(numbers)
print(result)  # Output should be [1, 2, 3, 4, 5, 6]  (Order might not be the same due to duplicates)
```

This Python script contains a self-contained function called `remove_duplicates`, which removes duplicates from a list of integers. The function utilizes a set data structure to keep track of seen integers, ensuring that each number is added only once. The function returns a result of the input list.