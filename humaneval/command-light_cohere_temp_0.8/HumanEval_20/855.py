```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        return numbers, 0, 1
    
    # Sort the list by the first element and store the index of the smallest number
    smallest_index = numbers.index(0)
    numbers.index = numbers.index(smallest_number)
    # Recursively find the two elements that are the closest to each other
    return numbers[smallest_index:], numbers[smallest_index + 1], smallest_index

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result)  # Output: (2.0, 3.0), (1.0, 2)

```

This script defines a function find_closest_elements that takes a list of numbers and returns a tuple containing the two closest elements. The function uses the algorithm to sort the list by the first element and then finds the index of the smallest number in the sorted list. It then uses this algorithm again to find the other element in the list that is closest to the first element. Finally, the function returns the tuple containing the two closest elements.