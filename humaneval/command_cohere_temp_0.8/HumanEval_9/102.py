Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found in the sequence up to that point. The function is designed to work with a list of integers, and the output is a list of integers of the same length as the input list, representing the rolling maximum elements at each position:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    max_so_far = numbers[0]
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)
    return rolling_max_list
```
The `rolling_max` function takes a list of integers `numbers` as input and initializes an empty list `rolling_max_list` to store the rolling maximum elements. It also sets `max_so_far` to the first element of the input list, which is the maximum element encountered so far.

Then, it iterates through the remaining elements in the `numbers` list using a `for` loop. For each element `num`, it compares it with the `max_so_far`. If `num` is greater than `max_so_far`, it updates `max_so_far` to `num`, thereby keeping track of the maximum element seen so far.

Finally, within the loop, it appends the value of `max_so_far` to the `rolling_max_list`. This process essentially keeps track of the maximum element encountered "until that moment" within the sequence, and the resulting `rolling_max_list` contains these rolling maximum elements.

The function is designed to work with a list of integers and will return a list of the same length as the input list, representing the rolling maximum elements at each position in the sequence. You can use the function to solve the problem statement provided. 

This function is generic and can be used with any list of integers to find the rolling maximum elements within the sequence.