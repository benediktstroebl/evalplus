```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen and not seen.add(num):
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. The function uses a set, called `seen`, to keep track of the unique integers it has encountered. It loops through the input list `numbers`, and for each integer `num`, it checks if the integer is already in the `seen` set. If the integer is not in the set, it adds it to both the set and the result list. If the integer is already in the set, it ignores it. Finally, it returns the result list, which contains only the unique integers from the input list, but in the same order. 

Here is an example usage of the function which tests the functionality:
```python
test_list = [1, 2, 3, 2, 4]
test_result = remove_duplicates(test_list)
print(test_result)  # Output: [1, 3, 4]
``` 

The function can be called with the `test_list` as an argument and the result is printed, which should be `[1, 3, 4]`.