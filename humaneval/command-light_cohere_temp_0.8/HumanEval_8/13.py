Here's the self-contained Python function that solves the problem:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: empty list
test_sum_product([])
shouldBe=(0,1)
# Test case 2: simple list
test_sum_product([1,2,3,4])
shouldBe=(10,24)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It uses a `typing` to ensure type safety. The function works by initializing `product` to 1 and then accumulating the sum and multiplying the numbers in the list. The function returns a tuple with the sum and product. 

The test cases demonstrate the expected behavior of the function. You can add more test cases as needed to ensure your function is working correctly.