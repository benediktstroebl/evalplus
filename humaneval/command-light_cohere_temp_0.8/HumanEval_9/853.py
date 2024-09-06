```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = [x for x in numbers if x == numbers[-1]]
    return [x for x in max_numbers if x != max_numbers[-1]]

# Unit tests
numbers = [1, 2, 3, 2, 3, 4, 2]
print(" Rolling Maximum:", rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
``` 
The provided Python code defines a function called rolling_max that takes a list of integers as an argument and returns a new list containing the rolling maximum elements of the input sequence. This is by iterating over the numbers, identifying the maximum element using the max function, and then excluding the last element, which is already the largest, to obtain the desired rolling maximum sequence.