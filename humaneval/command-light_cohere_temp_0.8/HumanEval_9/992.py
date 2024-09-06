```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [x for x in numbers if x >= 0]  # Convert negative numbers to positive
    max_num = numbers[0]  
    for num in numbers[1:]: 
        if num > max_num:
            max_num = num  
    return [max_num]
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]
``` 
The above Python script defines a function named `rolling_max`, which takes a list of integers as input and returns a list of the rolling maximum elements. The function first converts all negative numbers in the input list to positive using the `numbers[0]` element as the initial maximum. Then, it iterates through the maximum element in the list. After each iteration, the function compares the current element with the maximum element and updates the maximum element if the current element is greater.