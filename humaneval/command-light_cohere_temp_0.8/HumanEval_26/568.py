```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[:-len(seen)]]
    seen.add(numbers)
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
result_ref = remove_duplicates(numbers)
print("Result:", result_ref)

numbers_set = set(numbers)
print("Set result:", list(numbers_set))

```
The function `remove_duplicates` takes a list of integers as input and removes all elements that occur more than once. It achieves this by creating a set called `seen`, which keeps track of the elements that have been seen so far. Then, it iterates through the list `numbers` to find elements that are not in the `seen` set and not duplicates of elements that have already been seen. The `seen` set is updated with the new element, and the function returns the resulting list.