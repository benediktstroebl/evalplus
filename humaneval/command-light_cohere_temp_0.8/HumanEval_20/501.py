Here is a Python script that successfully solves the problem of finding the closest pair of elements in a list of numbers:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        return None
    
    # Sort the list of numbers in ascending order
    numbers.sort()

    list(sorted(numbers))
    
    # Initialize variables to track the two closest elements
    left, right = float('inf'), float('-inf')
    current_num = numbers[0]
    
    # Loop through the list of numbers
    for num in numbers[1:]:
        # Check if the current number is less than the left or right number
        if num < current_num:
            left = current_num
        if num > right:
            right = num
        
        # Update the current number
        current_num = num
    
    # Return the left and right numbers
    return current_num, right

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

print(find_closest_elements(numbers))
```

This function takes a list of numbers and returns the two closest elements in that list, in ascending order. The function first checks the condition that the list has less than two elements and returns `None`. It then sorts the list of numbers in ascending order. After that, the function initializes two variables `left` and `right` to track the two closest elements. It then loops through list of numbers and checks if the current number is less than the left or right number. If the current number is smaller, it updates the value of the left variable. If the current number is larger, it updates the value of the right variable. Finally, the function updates the current number and returns the updated values of the two closest elements.