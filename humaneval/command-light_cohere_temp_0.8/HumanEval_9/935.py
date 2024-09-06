```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort()
   
    max_num = numbers[0]
    current_max = max_num
    rolling_maxes = [current_max]

    for num in numbers[1:]:
        current_max = max(num, current_max)
        rolling_maxes.append(current_max)

    return rolling_maxes

# Test case 1
test_data = [1, 2, 3, 2, 3, 4, 2]
test_result = rolling_max(test_data)
print(test_result)

# Test case 2
test_data2 = [1, 3, 2, 4, 5]
test_result2 = rolling_max(test_data2)
print(test_result2)
```

The Python code defines a function called **rolling_max** that takes a list of integers as input and returns a new list containing the maximum element from the list after each rolling update. The function sorts the this input list and then iterates through each element, updating the maximum element to the current element. The function returns a list of these updated maximum elements. The code then includes two test cases, with different input lists, and prints the results of the rolling_max function applied to these test cases.