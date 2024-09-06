Here's a Python script that can solve the problem of finding the closest elements in a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # initializing variables
    l, r = 0, 1
    close_num, close_den = None
    
    # loop to find the smallest and largest elements in the list
    while l < len(numbers) and r < len(numbers):
        if numbers[l] < numbers[r]:
            close_num = numbers[l]
            close_den = 1
            l += 1
        else:
            close_num = numbers[r]
            close_den = 0
            r += 1
        
    # returning the two closest numbers
    return close_num, close_den

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]

find_closest_elements(numbers)
```

The script's find_closest_elements function takes a list of numbers and finds the two closest elements in that list. The function then returns the closest number and distance as a tuple.