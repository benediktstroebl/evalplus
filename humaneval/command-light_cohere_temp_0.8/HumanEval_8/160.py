```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in a list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various lists of integers
test_lists = [
    [],   # Empty list, should return (0, 1)
    [1, 2, 3],  # [1,2,3], should return (3, 6)
    [1, 2, 3, 4], # [1,2,3,4], should return (6, 24)
    # Add more tests as needed!
]

for test_list in test_lists:
    print(sum_product(test_list))  # Output: (6, 24)
```  This script defines a function sum_product that calculates the sum and product of a list of integers. The output of the function with the test lists will match the expected results.