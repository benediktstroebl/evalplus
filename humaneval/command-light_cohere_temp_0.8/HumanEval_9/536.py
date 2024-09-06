```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    max_ending = numbers[0]
    result = [max_so_far]
    for num in numbers[1:]:
        if num > max_ending:
            max_ending = num
        elif num > max_so_far:
            max_ending = num
        else:
            max_so_far = num
    result.max_ending,result.wait():
        return result
   have a new line? If you do not add the `max_ending` variable, the function will not return the correct result.