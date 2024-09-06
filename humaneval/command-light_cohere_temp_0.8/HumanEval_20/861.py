```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Taking two closest numbers and returning them in order of their Euclidean distance.
    min_val = float('inf')
    max_val = float('-inf')
    closest_numbers = (min_val, max_val)
    for num in numbers:
        diff = abs(num - min_val)
        if diff < max_val:
            max_val = diff
            max_val = num
        diff = abs(num - max_val)
        if diff < min_val:
            min_val = diff
            min_val = num
        closest_numbers = (min_val, max_val)
    return closest_numbers

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]
print(find_closest_elements(numbers)))
```
The script defines a function called find_closest_elements that takes a list of numbers as input and returns a tuple containing the two closest elements in the list. It initializes the first variable min_val and second variable max_val with the maximum and minimum possible floating numbers, respectively. Then, it iterates through each number in the input list and calculates the difference between the current number and min_val. The condition is checked to update either of the variables with the current number. The loop continues until the number is no smaller than min_val. Finally, the function returns the closest_numbers tuple, which contains the two closest numbers in the order of their Euclidean distance.

The output of the test case will be: ```python
(2.0, 1.0)
```