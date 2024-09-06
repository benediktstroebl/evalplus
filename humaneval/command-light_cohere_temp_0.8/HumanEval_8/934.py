```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case 1
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
assert result == (sum(test_data), product(test_data))
``` 
This function, sum_product, accepts a list of integers and outputs a tuple containing the list's sum and product. It achieves this result by iterating over the list, computing the product of each element by multiplying them together, and then adding the element to the sum. The test case 1 correctly demonstrates the