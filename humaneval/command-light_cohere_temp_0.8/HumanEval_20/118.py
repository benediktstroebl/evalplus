Here is the solution:

```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the numbers in ascending order
    numbers.sort(numbers)
    
    # Remove duplicates (keep only the first occurrence)
    numbers = [num for num in numbers if num not in [n for n in numbers for n != num]]
    
    # Initialize the first and second closest numbers
    first, second = float('inf'), float('-inf')
    for num in numbers:
        if num < first:
            first = num
        elif num > second:
            second = num
    
    # Return the first and second closest numbers
    return (first, second)
```

This function accepts a list of numbers as input and uses the "typing" module to define the input parameter as a "List[float]". The function sorts the input list of numbers in ascending order. Then, it eliminates duplicates (keeping only the first occurrence), and then it sets the first and second closest numbers to float('inf') and float('-inf') respectively, initializing the variables.

Finally, the function returns the first and second closest numbers as a tuple.