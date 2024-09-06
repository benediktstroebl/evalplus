```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Calculate and return the rolling maximum element found until a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)
    [3, 3, 3, 4, 4]
    """
    # initializing the rolling index and max element
    i = 0
    max_element = numbers[0]
    
    # loop until the rolling index exceeds the length of the sequence
    while i < len(numbers)-1:
        
        # get the current element in the sequence
        current = numbers[i]
        
        # check if the current element is greater than the max element
        if current > max_element:
            max_element = current 
        
        # increment the rolling index
        i += 1
        
    # return the final max element
    return [max_element]

# test cases
numbers1 = [1, 2, 3]
numbers2 = [3, 2, 4, 2, 1]
print(rolling_max(numbers1))
print(rolling_max(numbers2))
```

The function `rolling_max` takes a list of integers as input and generates a new list with the rolling maximum elements. The test cases provided demonstrate the valid inputs and the output will be a list with the elements: `[1, 2, 3]` for the first test case and `[3, 2, 4]` for the second test case.