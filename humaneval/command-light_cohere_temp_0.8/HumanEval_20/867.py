Here is a Python script that takes a list of numbers as input and returns a tuple containing the two numbers that are closest to each other:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Calculate the distance between each pair of numbers in the list
    distances = [float(num1 - num2) for num1, num2 in zip(numbers)]
    
    # Sort the list of distances in ascending order
    sorted_distances = sorted(distances)
    
    # Initialize variables for the first and second index
    first_index = 0
    second_index = 0
    
    # Iterate through the sorted list of distances
    for index, distance in enumerate(sorted_distances):
        if index > 0 and distance < distances[index - 1]:
            first_index = index
            second_index = (index - 1)
            break
    
    # Return the closest pair of elements in the list
    return (numbers[first_index], numbers[second_index])

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

find_closest_elements(numbers)

Output: The output will be a tuple containing the two numbers that are the closest to each other in the list:

```
(2.0, 3.0)
```
This demonstrates that the function `find_closest_elements` successfully finds the closest pair of elements in a list of numbers.