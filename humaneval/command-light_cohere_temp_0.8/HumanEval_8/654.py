```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    list comprehensions and type hinting in Python 3 and later make this particularly readable and clear.
    return (sum(numbers), *, product(numbers,))
    """
    return (sum(numbers), product(numbers,))

# Test cases
numbers = [1, 2, 3, 4]
print(sum_product(numbers))  # prints (10, 24)

numbers = []
print(sum_product(numbers))  # prints (0, 1)

numbers = [1, 2, 3, 4]
print(sum_product([x for x in numbers if x == 2]))  # 2 -> (2, 4)

numbers = [1, 2, 3, 4, 5]
print(sum_product(numbers[:2] + [5]))  # (6, 20)

numbers = [1, 2, 3]
print(sum_product([x for x in numbers if x == 2]))  # 2 -> (2, 6)
```