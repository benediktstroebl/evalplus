```python
from typing import List
def find_closest_elements(numbers: List[float]):
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    # Sort the numbers in ascending order
    numbers.sort()
    important to the other to determine the order of closest elements
    # Initialize the closest elements to None, as we don't know which elements are the closest yet
    result = [None, None]
    for i in range(len(numbers) - 1):
        current = numbers[i]
        next = numbers[i + 1]
        if current > next:
            result[0], result[1] = next, current
    return result
```
The function `find_closest_elements` takes a list of numbers as an input and returns a tuple of the two closest numbers in the list. The function first checks if the list has at least two elements, and if it doesn't, raises a `ValueError`. If the list has at least two elements, the function sorts the list in ascending order and then uses a for loop to compare each number with the next number in the list to determine which number is the closest. The function then initializes the result with the two elements being None, and then uses a while loop to compare each element in the list with the next until the loop reaches the first element in the list. Finally, the function returns the result, which contains the two closest elements in the list, in order from smaller to larger number.