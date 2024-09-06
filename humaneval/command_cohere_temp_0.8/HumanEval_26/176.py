```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes all elements that occur more than once in a list of integers
        Returns a new list without duplicates, keeping the order of elements.
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input. It removes any elements that occur more than once and returns a new list with only the unique elements. To do this, it uses a set called `seen` to keep track of elements that have already been encountered. Then, it appends elements to the `result` list if they have not been marked as seen, thereby removing duplicates. 

The script ensures that the order of elements in the input list is preserved in the output list. 

Could I assist you in any other way? If you would like, I can provide you with tests that you can use to validate the functionality of this script.