```python
from typing import List
def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    # Initialize the closest elements
    closest = [float("inf")] * 2 for i in numbers]
    # Initialize the current number
    current = 0
    # Loop through the numbers in the list
    for num in numbers:
        # If the current number is smaller than the current closest element, update the current closest element
        if current > num:
            current = num
        # If the current number is equal to the current closest element, keep it
        elif current == num:
            continue
        # Update the closest elements list with the current number
        closest.append(current)
    return closest
```

This Python code defines a function called `find_closest_elements` that takes a list of floating-point numbers as input and returns a tuple containing the two closest numbers in the list, along with their relative difference. The function sorts the previous list, and then iterates through the sorted list to find the two closest numbers. The function compares each number in the list to the current number and updates the current number if a smaller number is found. If the current number is equal to the current closest number, the function continues iterating. The function then returns the two closest numbers, which are the smallest and largest numbers in the sorted list, along with their relative difference.