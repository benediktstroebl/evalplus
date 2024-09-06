Here is a Python script that includes a self-contained function that solves the problem you provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize the first and second closest values
    first, second = None, float('-inf')
    
    # Sort the numbers based on their first element
    numbers.sort(key=lambda num: num[0])
    sorted_numbers = [num[0] for num in numbers]
    
    # Initialize the first and second closest numbers
    for i in range(len(sorted_numbers)):
        if sorted_numbers[i] < first:
            first = sorted_numbers[i]
        if sorted_numbers[i] < second:
            second = sorted_numbers[i]
            
    return (first, second)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)

# Output:
```

The output will be a tuple that contains the two closest numbers in the supplied list, returned in that order (smaller number, larger number).