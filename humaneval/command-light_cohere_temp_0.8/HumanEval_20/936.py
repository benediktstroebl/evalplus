```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # initialising variables
    min_val: float = float('inf')
    max_val: float = -float('inf')
    closest_num: float = float('-inf')
    closest_index: int = -1
    
    # loop to compare and find closest number
    for index in range(len(numbers)):
        current_num:
            # current number in the list
            if current_num < min_val:
                min_val = current_num
                closest_index = index
            elif current_num > max_val:
                max_val = current_num
                closest_index = index
            else:
                # current number equals the closest so far, but we keep going to improve accuracy
                if current_num < closest_num:
                    closest_num = current_num
                    closest_index = index
    
    return (min_val, max_val), closest_index

```
The function takes a list of numbers and returns a tuple of two floats, with the first value being the smaller of the two numbers and the second being the larger. The function can also be tested with the following:
```
from typing import List

def find_closest_elements(numbers: List[float]):
    # initialising variables
    min_val: float = float('inf')
    max_val: float = -float('inf')
    closest_num: float = float('-inf')
    closest_index: int = -1
    
    # loop to compare and find closest number
    for index in range(len(numbers)):
        current_num:
            # current number in the list
            if current_num < min_val:
                min_val = current_num
                closest_index = index
            elif current_num > max_val:
                max_val = current_num
                closest_index = index
            else:
                # current number equals the closest so far, but we keep going to improve accuracy
                if current_num < closest_num:
                    closest_num = current_num
                    closest_index = index
    
    return (min_val, max_val), closest_index

```
This should return the correct answer for the given prompt.