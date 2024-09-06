```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(numbers)
    result = [x for x in numbers if x == numbers[0]]
    return [x for x in result if x != numbers[0]] + [numbers[0]]
``` 
The function takes a list of integers as input and uses list comprehension to find the first element in the list, which corresponds to the maximum value. The function then generates a list of rolling maximum elements found until the first moment in the sequence by using a list comprehension that iterates through the list of numbers and includes elements that are equal to the first element in the sequence, as well as the first element itself. 
Then, the function returns a list of rolling maximum elements and the first element from the input list.