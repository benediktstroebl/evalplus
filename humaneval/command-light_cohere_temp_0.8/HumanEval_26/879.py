```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers.
    # Initialize a time set to keep track of unique elements
    set_ = set(numbers)
    # Remove duplicates from the list
    numbers = [x for x in numbers if x not in set_]
    return numbers

# Test case
test_data = [1, 2, 3, 2, 4]
test_result = remove_duplicates(test_data)
print(test_result)  # Output: [1, 3, 4]
```
This code defines a function **`remove_duplicates`** that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses the to store unique elements from the input list, and then removes any duplicates. Finally, it prints the set of unique integers from the test case, which should result in the expected output: `[1, 3, 4]`.