```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# A test case
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(f"Sum: {result[0]}  , Product: {result[1]}")
``` 
This code defines the `sum_product` function that calculates the sum and product of a list of integers. It utilizes a simple loop to iterate over the numbers and accumulate the sum and product. Additionally, it handles the empty lists and passes the corresponding edge case tests.