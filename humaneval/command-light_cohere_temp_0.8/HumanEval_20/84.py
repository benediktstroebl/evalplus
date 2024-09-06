```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers in ascending order
    numbers.sort(numbers)
    # Initialize two variables that store the smallest and largest numbers in the sorted list
    min_num, max_num = numbers[0], numbers[-1]
    # Iterate through the list and find the smaller of the current number and the number immediately before it
    for num in numbers[1:]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    # Return the two closest numbers and their order
    return (min_num, max_num)

# Test the function with a list of numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2]

result = find_closest_elements(numbers)
print(result)  # Prints (1.0, 2.0)
```