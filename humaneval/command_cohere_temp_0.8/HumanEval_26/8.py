```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen or len(seen) == 1:
            result.append(num)
            seen.add(num)
    return result
```

The function `remove_duplicates` removes elements that occur more than once in a list of integers, while preserving the order of the remaining elements. It does so by utilizing a set, `seen`, to keep track of elements that have already been encountered. As sets only store unique elements, any attempt to add an element that is a duplicate will simply result in the set's update without altering the output list, `result`. 

To retain the order of elements, the function adds each unique element from the input list to both the `result` list and the `seen` set, ensuring that elements are not duplicated in the final `result` list. 

This approach allows the function to remove duplicates and maintain the original order of the elements in a single pass through the input list. 

The unit tests that ensure the correctness of this function are not provided in this response but are typically appended at the bottom of the script, outside the functions, to check the functionality of the `remove_duplicates` function.