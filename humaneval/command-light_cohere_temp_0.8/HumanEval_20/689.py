```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # Sort the list of numbers
    numbers.sort(numbers)
    
    # Get the two closest elements from the sorted list
    smaller_num, larger_num = (numbers[0], numbers[-1])
    for i in range(1, len(numbers)-1):
            if numbers[i] < numbers[i-1]:
                smaller_num, larger_num = (numbers[i], numbers[i-1])
    return smaller_num, larger_num

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]

result = find_closest_elements(numbers), [lambda n: n is float])
print(result)
```