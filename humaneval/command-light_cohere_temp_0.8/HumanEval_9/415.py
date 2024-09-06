```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Calculate the rolling maximum element in a list of integers
    >  Return a list of the maximum element found in the list so far, and the index of the list where it was found. 
    """ 
    - Initialize two variables: 
    - m - current index of maxima 
    - max_num - current max value 
    - arr - list of numbers 
    > Iterate through the list: 
    - If m is less than len(arr), increment m and assign max_num to the last element in arr[m]. 
    - If m is now len(arr), m is done, and assign max_num to the last element in arr[m-1]. 
    > Return a tuple with the list of max elements and their index 
    """
    max_num, m = 0, 0
    arr = numbers
    while m < len(arr):
        if arr[m] > max_num:
            max_num, m = arr[m], m
        m += 1
    return [max_num, m]
```