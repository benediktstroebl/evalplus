```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        elif num == max_num and max_count < 3:
            max_count += 1
    return [max_num for _ in range(max_count)]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
``` 
This code defines a function `rolling_max` that takes a list of integers as an argument and returns a list of the maximum elements after rolling them, with the number of appearances of each maximum element limited to 3. 
The function uses a `max_count` variable to keep track of the number of times the current maximum element has been encountered, and it updates this variable whenever a new maximum element is found. 
The `numbers` list is then passed to the function and `result` is printed, which contains the list of maximum elements after rolling.