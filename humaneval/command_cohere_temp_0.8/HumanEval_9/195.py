Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at any given moment in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    max_tracker = numbers[0]
    max_list = [max_tracker]
    for num in numbers[1:]:
        if num > max_tracker:
            max_tracker = num
            max_list.append(max_tracker)
        else:
            max_list.append(max_tracker)
    return max_list

# Test Cases
numbers_list = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers_list)
print(result)
```
This script defines the `rolling_max` function, which takes a list of integers (`numbers`) as input. It initializes `max_tracker` to the first element of the list and `max_list` to store the rolling maximums encountered so far. The loop iterates through the list, comparing each element to the current `max_tracker`. If an element is greater, it updates both `max_tracker` and `max_list`. Otherwise, it appends the previous `max_tracker` to `max_list`. This effectively generates a list of rolling maximums up to each point in the sequence. The test case provided in the script uses the input list `[1, 2, 3, 2, 3, 4, 2]` and prints the expected output `[1, 2, 3, 3, 3, 4, 4]`. 
When executed, the output of the script will be:
```
[1, 2, 3, 3, 3, 4, 4]
``` 
This is the expected output of the rolling_max function for the provided test case. Mention that you can use this function on lists of numbers to find the rolling maximum for any given list. 
If you have any questions, let me know! I'm here to help.