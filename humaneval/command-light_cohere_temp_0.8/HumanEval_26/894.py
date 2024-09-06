```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()] and not seen.

# Sample input
numbers = [1, 2, 3, 2, 4, 3, 2, 1]

# Call the remove_duplicates function and store the result in a variable
result = remove_duplicates(numbers)

# Print the result
print(result)
```

This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicates removed. The result is then stored in the variable result and finally, printed to the console.