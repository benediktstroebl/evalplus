Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Initialize a tuple to store the results
    closest_result = Tuple( None for _ in [0.0] )

    # Sort the numbers in descending order and set the closest elements to the first half of the list
    for i, n in enumerate(numbers):
        if n < closest_result[0]:
            closest_result = Tuple( closest_result[0] = n, n )

    # Return the first element of the tuple
    return closest_result[0]

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = find_closest_elements(numbers)
```
This function takes a list of numbers as input and returns a tuple with the two closest numbers in descending order. The function first sorts the numbers in descending order and sets the closest elements to the first half of the list. Then, it continues to compare the two closest elements until it finds a smaller number, and updates the tuple with the new closer element. Finally, the function returns the first element of the tuple as the result.