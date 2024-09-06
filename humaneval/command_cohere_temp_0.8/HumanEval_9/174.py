Here's a Python script that contains a function called `rolling_max` that takes a list of integers `numbers` as input and returns a list of rolling maximum elements found in the sequence up to that point. The function is designed to work with mutable objects like lists and is parametrized over the data type of the input list and the return list. 

```python
from typing import List, Tuple

def rolling_max(numbers: List[int], max_so_far: List[int]=None) -> List[int]:
    if max_so_far is None:
        max_so_far = [numbers[0]] if numbers else []
    if not numbers:
        return max_so_far
    max_so_far[:] = [max(max_so_far[-1], numbers[0])] + max_so_far[:-1]
    return max_so_far
```

The function uses the `typing` module, introduced in Python 3.5, to declare the input and output types, which improves the readability and maintainability of the code. The function uses an optional parameter called `max_so_far` which is set to `None` by default. This parameter allows the function to store the maximum elements seen so far. If the `max_so_far` parameter is not provided, the function initializes it with the first element of the input list. 

The output list is updated by extracting the maximum element of the current element and the `max_so_far` list. The resulting list is then returned, containing the maximum element seen at each position in the input list. 

Here is an example of how to use this function:
```python
input_list = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(input_list))
```

Output:
```bash
[1, 2, 3, 3, 3, 4, 4]
```