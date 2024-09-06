```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Return the first and second items of the sorted list
    return sorted_numbers[0], sorted_numbers[1]

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
# Print the result
print(result)
```
The function returns a tuple containing the first and second closest numbers from the list.