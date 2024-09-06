```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from the given list.

    : Parameters: 
        numbers = [int for i in range(0, len(n))] 
    Returns: 
        List[int], the list of maximum elements in rolling manner. 
    """
   
    List[int] = [x for x in numbers if x > numbers[x]]
    return List[int][::-1]  # return the reversed list of rolling maximum elements

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
assert len(result)==7 and all(result == [x for x in numbers if x > numbers[x]]), result == [1, 2, 3, 3, 3, 4, 4])

# Test case 2
numbers = [1, 1, 2, 3, 4, 5]
result = rolling_max(numbers)
assert len(result)==5 and all(result == [x for x in numbers if x > numbers[x]]), result == [1, 2, 3, 4])

# Test case 3
numbers = [1, 9, 10, 1, 2, 3]
result = rolling_max(numbers)
assert len(result)==5 and all(result == [x for x in numbers if x > numbers[x]]), result == [1, 2, 3, 10])
```
This script defines a function `rolling_max` that calculates the rolling maximum elements in a list. The function uses a list comprehension to select the largest number until the current index reaches the length of the list. Additionally, the `List[::-1]` method is used to reverse the order of the elements. The test cases demonstrate the usage of the function with different input lists and validate the expected output.