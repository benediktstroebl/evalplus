Here is a self-contained Python script that solves the problem of finding the closest elements from a supplied list of numbers:

```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Define the two closest elements and sort them based on their magnitudes.
    smallest = float('inf')
    largest = float('-inf')
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    # Return the two closest elements in order, as a tuple
    return (smallest, largest)

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print_closest_elements(numbers)
```

In this code, the find_closest_elements function takes a list of numbers as an input parameter and uses two variables, smallest and largest, to keep track of the two closest elements. It iterates through them through the list and compares the values of each element with the current values of smallest and largest. The first element that is smaller is assigned to smallest, and the first element that is larger is assigned to the largest variable. 

Finally, the function returns a tuple containing the two closest elements, which are stored in the order of their smaller and larger values.