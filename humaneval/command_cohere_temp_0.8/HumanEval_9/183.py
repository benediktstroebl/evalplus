```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    rolling_maxes = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_maxes.append(numbers[i])
        else:
            rolling_maxes.append(rolling_maxes[-1])
    return rolling_maxes
```

The algorithm for the code is based on the following steps:
1. Initialize a list `rolling_maxes` to store the rolling maximums with the first element of the input `numbers` list.
2. Iterate through the list, and for each element, compare it with its previous element.
3. If the current element is greater than its previous, add it to the `rolling_maxes` list.
4. If the current element is less than or equal to its previous, add the previous maximum to maintain the rolling effect.
5. After iterating through all elements, the `rolling_maxes` list will contain the rolling maximum elements.

The script ensures that even with small lists, the algorithm still functions correctly, as the rolling max calculation is not affected by the size of the list like subsequence searches or median calculations could be. 

To better understand the code, here is an example of how to use the function:
```python
test_list = [1, 2, 3, 2, 3, 4, 2]
print("The rolling max for the list", test_list, "is:", rolling_max(test_list))
``` 

The output will be:
```
The rolling max for the list [1, 2, 3, 2, 3, 4, 2] is: [1, 2, 3, 3, 3, 4, 4]
```

This list contains the maximum elements that evolve throughout the original list sorted in the order they are displayed.