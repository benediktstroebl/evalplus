Here's a Python script that contains a function called `rolling_max` which takes a list of numbers and returns a list of the rolling maximum values found in the sequence up to that point. The function is described by the following type of statement:
```python
def rolling_max(numbers: List[int]) -> List[int]:
```

The solution uses a sliding window approach to find the rolling maximum in a list of numbers. Here's the code:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_list = [numbers[0]]

    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        max_list.append(max_so_far)

    return max_list
```

The given example in the problem statement returns the following when applied to the function:
```python
>>> rolling_max([1, 2, 3, 2, 3, 4, 2])
[1, 2, 3, 3, 3, 4, 4]
``` 

This approach uses a first element responsive algorithm that slides through the list and generates a list of maximum elements up to that point in time.  An initial max_so_far variable and max_list are initialized with the first element of the list. The sliding window approach then compares the currently analyzed element with the maximum observed so far, if the currently analyzed element is greater than the one observed so far, then max_so_far is updated, and the updated max is added to the max_list. Lastly, the max_list is returned, which contains the rolling maximums for the given list.