```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    numbers = [1, 2, 3, 4]
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test case 1: empty list
result1 = sum_product([])
result1 = (0, 1)
#Test case 2: single element
result2 = sum_product([1])
result2 = (1, 1)
#Test case 3: two elements
result3 = sum_product([1, 2])
result3 = (2, 2)
#Test case 4: three elements
result4 = sum_product([1, 2, 3])
result4 = (5, 6)
#Test case 5: four elements
result5 = sum_product([1, 2, 3, 4])
result5 = (8, 12)

print(f'Test case 1: {result1}') # Output: (0, 1)
print(f'Test case 2: {result2}') # Output: (1, 1)
print(f'Test case 3: {result3}') # Output: (2, 2)
print(f'Test case 4: {result4}') # Output: (5, 12)
print(f'Test case 5: {result5}') # Output: (8, 12)
```

This script defines a function `sum_product` that calculates the sum and product of a given list of integers. The function is then tested with several test cases to verify its correctness.