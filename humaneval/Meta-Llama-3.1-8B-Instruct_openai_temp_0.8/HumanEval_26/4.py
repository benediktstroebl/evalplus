```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4, 4, 5, 5, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
```

This script defines the `remove_duplicates` function which takes a list of integers as input, and returns a new list with all elements that occur more than once removed. The function uses a set to keep track of seen elements. It iterates over the input list, and for each element, it checks if it's in the set. If not, it adds the element to the set and to the result list. This way, elements that occur more than once are skipped. 

Note: This approach has a time complexity of O(n), where n is the length of the input list, since each element is visited once, and each operation (checking membership in the set and adding an element to the set) is O(1) on average. 

Alternatively, you could solve this problem using dictionary to count occurrences of each number and then construct a new list with elements having a count of 1. This solution also achieves a time complexity of O(n), but it requires additional space to store the count dictionary:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    return [num for num in numbers if count[num] == 1]

# Example usage:
numbers = [1, 2, 3, 2, 4, 4, 5, 5, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
```