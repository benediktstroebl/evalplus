Here is a Python script that solves the problem of finding the maximum element in the rolling sequence using the rolling_max function:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_counter = 0
    current_max = numbers[0]
    max_elements = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif current_max < num and max_counter == 0:
            max_counter += 1
        else:
            max_elements. Max elements elements number maximum number of elements.
    return max_elements

# Test cases
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 2, 3, 4, 1]
numbers3 = [6, 7, 8, 9, 6]

print("Test Case 1:", rolling_max(numbers1))
print("\n")

print("Test Case 2:", rolling_max(numbers2))
print("\n")

print("Test Case 3:", rolling_max(numbers3))
print("\n")
```
The `rolling_max` function uses a counter to track the maximum element found so far. The counter is incremented when a new element is larger than the current maximum. The maximum element is stored in the `max_elements` list and returned at the end.