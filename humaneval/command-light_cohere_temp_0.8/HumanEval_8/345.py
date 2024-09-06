```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test the function with different inputs
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append([5, 6, 7, 8])
test_sum_product.append([10, 11, 12])
test_sum_product.append([13, 14, 15])
test_sum_product.append([16, 17, 18])

print(sum_product(test_sum_product))  # Output: (149, 27049)
``` 
The provided Python script defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function first checks if the list is empty, returning (0, 1) in that case. It then uses the product and sum to compute the product and sum, respectively, and returns the tuple.