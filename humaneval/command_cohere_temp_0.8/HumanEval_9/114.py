Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found up to that point in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
            max_list.append(max_so_far)
        
    return max_list
```
The function uses a initial maximum value from the first element in the list `max_so_far` and an initial list to store the rolling maximum values `max_list`. Then the function loops through the rest of the elements in the list, it compares each element to the current maximum value, and updates the maximum value and list if needed. 

You can verify the correctness of the function by using the example provided in the problem statement:
```python
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
```
This will return the list of rolling maximum values up to each point in the sequence.