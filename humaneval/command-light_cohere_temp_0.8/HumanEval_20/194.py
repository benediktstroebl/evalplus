Here is a self-contained Python script that solves the problem of finding the closest elements in a list of numbers:
```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # sort the list
    sorted_numbers = sorted(numbers)
    # find the two closest numbers
    i = 0
    j = len(sorted_numbers) - 1
    while i < j:
        current_num = sorted_numbers[i] + sorted_numbers[j]
        if current_num < numbers[0] + numbers[1]:
            numbers = [current_num] + [numbers[0]] + [numbers[1]]
            i += 1
        elif current_num > numbers[-1] + numbers[-2]:
            j -= 1
        else:
            break
    return numbers
```
This function takes a list of numbers and sorts it. Then it iterates through two pointers, one starting at the first element and the other starting at the second last element, and repeatedly update these pointers to find the two closest numbers.