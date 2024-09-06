Here's the self-contained function along with test cases: 

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list """
    if not numbers:  # empty list case
        return (0, 1)
    total, prod = [], 1
    for num in numbers:
        total.append(num)
        prod *= num
    return (sum(total), prod)
# test case 1
print(sum_product([1, 2, 3, 4])) # (10, 24)
# test case 2
print(sum_product([10, 20, 30, 40])) # (60, 120)
```