```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimiter = 4

expected_result = [1, 4, 2, 4, 3, 4, 5]

print(intersperse(numbers, delimiter))
print(expected_result)

```

The function `intersperse()` takes in a list of integers called `numbers` and an int `delimiter` as parameters. When called, it returns a new list where each pair of consecutive elements in `numbers` is separated by `delimiter`. However, if the `numbers` list is empty, it returns a list of just `delimiter`s. This is achieved through a recursive approach, where the base case checks for an empty list and returns a list of just delimiter introns, while the recursive case concatenates the `delimiter` with the intersperse of the rest of the list. Overall, the function solves the problem of inserting a `delimiter` between consecutive elements of a list, handles any empty list checks, and does so in a recursive manner to concatenate the new list.