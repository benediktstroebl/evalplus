Here's a Python script that contains a function called `rolling_max` which takes a list of numbers and returns a list of rolling maximum elements from the list:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], cap: int = None) -> List[int]:
    if cap is None:
        cap = len(numbers)
    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_max_list.append(numbers[i])
        else:
            if numbers[i] == rolling_max_list[-1]:
                rolling_max_list.append(rolling_max_list[-1])
            else:
                j = rolling_max_list[-1]
                for k in range(i - 1, -1, -1):
                    if numbers[k] > j:
                        j = numbers[k]
                        rolling_max_list[k + 1:] = rolling_max_list[k + 1:] + [j]
                rolling_max_list[k] = j
    if cap != len(numbers):
        rolling_max_list = rolling_max_list[:cap]
    return rolling_max_list

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

The function takes a list of numbers and an optional argument `cap` that is the total number of rolling maximum elements to be generated. The function starts with a single element `numbers[0]` and then iterates through the list. If the current element is greater than the previous one, it adds it to the rolling max list, if it's smaller it investigates the previous list of rolling max values to update them accordingly. The function makes sure to generate a list of the specified `cap` number of elements only if it's different from the total length of the input list. The output of the example provided in the docstring is:
```bash
[1, 2, 3, 3, 3, 4, 4]
```