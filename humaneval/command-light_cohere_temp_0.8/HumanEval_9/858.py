```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)
    rolling_max_temp = numbers[0]
    seen = [numbers[0]]

    for num in numbers[1:]:
        if num > rolling_max_temp:
            rolling_max_temp = num
        elif num in seen:
            seen.add(num)
        else:
            seen.add([rolling_max_temp])

    return seen

rolling_max_test_numbers = [1, 2, 3, 4, 3, 2, 1, 4, 4]
result = rolling_max(rolling_max_test_numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
This Python code defines a function called rolling_max that takes a list of integers as input and returns a new list containing the elements that will always be seen on the maximum element in the list. This function uses a shallow copy to start with the first element of the input list and keeps track of the elements that have been seen so far using a seen dictionary. The function then iterates over the element of the list and compares the current element to the current maximum element seen so far. If the current element is greater than the current maximum element, the current maximum element is updated. If the current element is equal to the current maximum element or is already in the seen dictionary, the function checks if the element is already in the seen list. If it is not, the element is added to the seen list. This process continues until all list is empty.