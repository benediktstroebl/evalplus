```python
from typing import List

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Find the two closest elements and return them in order
    smaller_num, larger_num = (numbers[0], numbers[1])
    while len(numbers) > 1:
        next_num = numbers[2]
        if next_num > larger_num:
            larger_num, next_num = next_num, numbers.
            numbers = numbers[drop:3:]
        else:
            smaller_num, next_num = next_num, numbers[0]
            numbers = numbers[drop:3:]
    
    return smaller_num, larger_num
```