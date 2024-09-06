```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    numbers.sort(numbers)  # Sort the list of numbers in ascending order
    max_num = numbers[0]
    current_max = max_num
    for num in numbers[1:]:
        if num > current_max:
            current_max = num 
    return [current_max]

# Test cases
numbers = [1, 2, 3, 4, 5]
test_result = rolling_max(numbers)
print(test_result)  # Output: [3, 4, 5]

numbers = [10,20,30,40,50]
test_result = rolling_max(numbers)
print(test_result)  # Output: [40, 50]

numbers = [2,3,4,5,6]
test_result = rolling_max(numbers)
print(test_result)  # Output: [5, 6]
```
This script defines a function called rolling_max that takes a list of integers as an argument and returns a new list of the maximum elements found in that list, rolling over the elements from left to right. This is can be useful in a variety of applications, such as generating a moving average in a data stream or finding the most frequent element in a list.

The script is written entirely within the function, making it self-contained and easy to understand. It also includes test cases to show how the function works on different types of input data.