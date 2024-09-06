```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]  # melted set of numbers]
```
This function takes a list of integers as input and returns a new list with all the integers in the input list, except for those that already appear in the set of numbers. 
The function is self-contained, as it does not need to access any other modules or functions to solve the problem. 

Note that the function uses the set() method to create a set of the numbers in the input list.