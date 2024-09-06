```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case 1: Should return (10, 1)
print(sum_product([1, 2, 3, 4]))

# Test case 2: This will cause an empty list exception
print(sum_product([]))

# Test case 3: Should return correct sum and product
print(sum_product([1, 2, 3, 4, 5]))
``` 
This Python script defines a function sum_product that calculates the sum and product of a list of integers. The function first checks if the list is empty and returns 0 and 1 as product and sum respectively. It then calculates the general sum and product of a list of integers using the sum and product functions respectively and returns the result as a tuple.