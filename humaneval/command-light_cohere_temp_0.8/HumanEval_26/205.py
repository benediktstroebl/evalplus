```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
``` 
This function, `remove_duplicates`, utilizes the `set()` function to create a unique set of integers from the input list. 
To ensure the result is correct, it is tested with a sample input.