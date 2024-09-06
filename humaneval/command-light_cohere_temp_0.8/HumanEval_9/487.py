```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A utility function to find the rolling maximum element in a given list of integers.
    The list of numbers is passed as an argument
    Returns a list with the rolling maximum elements.
    """
    list is sorted() and a counter for the index of the maximum element.
    The maximum element is returned and the counter is increased.
    """
    numbers.
    counter = 0
    max_element = numbers[0]
    result = [max_element] counter += 1
    for i in range(1, len(numbers)):
        if numbers[i] > max_element:
            max_element = numbers[i]
        result.append(max_element) counter += 1
    return result

# Test cases
numbers1 = [3, 2, 4, 1, 10, 3]
numbers2 = [5, 6, 7, 8, 9, 10]
numbers3 = [21, 22, 19, 33, 34]

result1 = rolling_max(numbers1)
print("Result 1:", result1)

result2 = rolling_max(numbers2)
print("Result 2:", result2)

result3 = rolling_max(numbers3)
print("Result 3:", result3)
```
This code defines the rolling_max function that takes a list of integers and returns a list of the maximum elements found in the sequence as they roll, it then passes these test cases to test the function's functionality.