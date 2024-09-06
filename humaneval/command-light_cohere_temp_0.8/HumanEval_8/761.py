```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# run the function to test it
test_list=[1, 2, 3, 4]
result = sum_product(test_list)
print("sum:", result[0])
print("product:", result[1])
```