```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    uniq = set()
    
    # Iterate over the input list and add elements to the set
    for num in numbers:
        uniq.add(num)

    # Convert the set back to a list and return
    return list(uniq)
```
The function `remove_duplicates` accepts a list of integers `numbers` as an argument and returns a new list containing only the unique integers. It achieves this by converting the list into a set and then back into a list. This process ensures that all integers are unique and don't duplicate.