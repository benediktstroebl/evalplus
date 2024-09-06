```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Initialize data structures
    min_val = float('inf')
    min_idx = None
    max_val = 0
    max_idx = numbers[0]

    # Sort the list of numbers
    numbers.sort(key=lambda num: num)
    numbers.sort()

    larger_num = 0
    smaller_num = float('inf')

    for idx, num in enumerate(numbers):
        if num < smaller_num:
            smaller_num = num
            smaller_idx = idx
        elif num > larger_num:
            larger_num = num
            larger_idx = idx

    # Return two numbers that are closest to each other
    return (smaller_num, smaller_idx), (larger_num, larger_idx))

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 2.0]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

numbers = sorted(numbers, key=lambda num: num)

result = find_closest_elements(numbers)

print("The two closest numbers are:", result[0][0], result[1][0])
```
This function takes a list of numbers and returns a tuple of the two closest numbers, along with their respective indices in the original list. It also handles cases where the numbers are in the correct order, so the function will still return the correct result.