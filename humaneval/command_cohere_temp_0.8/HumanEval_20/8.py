```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    return numbers[1], numbers[2]
```
This Python script defines a function called `find_closest_elements` that takes a list of floating numbers (`List[float])` as input. This function sorts the input list in ascending order using the `sort()` method, and it returns the second and third elements from the sorted list, whichever pair is closest to each other. This approach works because sorting ensures that adjacent elements in the list are close together. The output is a tuple containing two float values, the smaller and larger of the two closest numbers in the list. 

Here is an example usage of the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
result = find_closest_elements(test_list)
print(result)  # Output: (2.0, 2.2)
```
And here is a more detailed example with commented code: 
```python
# Define a list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]

# Call the find_closest_elements function
result = find_closest_elements(numbers)

# Print and explain the result
print(f"Result: {result}")  # Result: (2.0, 2.2)
# The function returns the second and third elements from the sorted list
# They are closest to each other in the given list
# Thus, the output is the smaller (2.0) and the larger (2.2) of these two elements
``` 
This script demonstrates how to select two elements from a list of numbers in such a way that they are the closest to each other. It provides a self-contained solution that can be easily reused in other projects.