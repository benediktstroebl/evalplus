```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Define function to find two closest elements
    def closest_pair(arr):
        # Sort array in descending order
        arr.sort(arr, reverse=True)
        # Initialize min and max values to the first and last elements
        min_val = arr[0]
        max_val = arr[-1]
        # Loop through the array and update min and max values
        for i in range(1, len(arr)):
            current_val = arr[i]
            if current_val < min_val:
                min_val = current_val
            elif current_val > max_val:
                max_val = current_val
        return min_val, max_val

    # Return two closest elements
    return closest_pair(numbers)

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
print_closest_elements(numbers)
```

This script defines a function find_closest_elements that takes in a list of numbers and returns a tuple containing the two closest numbers in order. The function uses a sorted numbers in descending order and iterates through the array to find the smallest and largest values. The function then returns the two closest numbers.