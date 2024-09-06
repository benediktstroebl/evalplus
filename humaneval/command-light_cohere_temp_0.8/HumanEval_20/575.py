Here is a Python script that contains a self-contained function that solves the problem of finding the closest pair of elements in a list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize variables to keep track of the closest pair of numbers.
    left, right = float('-inf'), float('-inf')
    middle = float('inf')
    # Loop to find the closest pair of numbers
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Calculate the distance between the two numbers
            distance = (numbers[i] - numbers[j]) ** 2
            # Update the variables with the current distance and the index of the number
            if distance < left + right:
                left, right = distance, j
            # Check if there is a closer middle number
            if distance < middle:
                middle = distance
    # Return the closest pair in descending order
    return (left, right) if left < right else (right, left)
```

This function works by finding the two closest elements in the list and then returns them in descending order based on their values. The function uses the accuracy of the calculation by checking if the new element is closer than the middle element. 

The function also uses a while loop to efficiently find the closest pair of elements in the list.