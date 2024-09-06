```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_element = numbers[0]
    result = [max_element]
    
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
        elif num > max_so_far:
            max_so_far = num
    
    for num in numbers:
        if num == max_element:
            break  # stop searching for the same element again
        result.append(max_element)
        return result
```
This Python code defines a function called `rolling_max` that takes a list of integers as input and generates a new list containing the running maximum elements found within the input sequence up to the current moment. The code uses the first initializes the maximum value and the current element with the initial element of the input list. It then iterates through through each element in the list, compares it with the current maximum value, and updates the maximum value if the current element is greater. The code also updates the maximum value if it is greater than the current maximum seen so far (`max_so_far`). This process continues until all elements in the list have been compared to the current maximum value. The code then returns the array of integers representing the running maximum elements in the input sequence.