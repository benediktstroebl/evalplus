```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]  #copy.from collections.set()
 specifically creates a unique set of elements from the list.

```

In this script, we use the `set()` function to create a set of elements from the input list. The `not in` condition checks if an element from the input list is already in the set, which means it's a duplicate. The `copy.from()` method creates a unique set of elements from the input list, which includes all the elements from the list.

Finally, we use a list comprehension to filter out the duplicate elements from the input list, resulting in a new list with only the unique elements.