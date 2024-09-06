Here is the solution:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Get the two closest numbers
    first_index = next((i for i, num in enumerate(sorted_numbers) if num != sorted_numbers[i] and num != sorted_numbers[i+1]), 0)
    second_index = next((i for i, num in enumerate(sorted_numbers) if num != sorted_numbers[i] and num != sorted_numbers[i-1]), 0)
    
    # Return the two closest numbers in order
    return Tuple(sorted_numbers[first_index], sorted_numbers[second_index])
```
This function takes a list of numbers and returns a tuple containing the two closest numbers in that list. It uses the sorted() function to sort the list of numbers, then uses the next() function to find the first and second indices of the two closest numbers. The function then returns the the two closest numbers in order.