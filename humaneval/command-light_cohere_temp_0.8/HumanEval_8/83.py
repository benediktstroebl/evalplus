```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 1
    product = 1
    for num in numbers:
        result *= num
        product += num
    return (result, product)
test_sum_product = [1, 2, 3, 4]
test_empty_list = []
test_single_number = 4

results = sum_product(test_sum_product)
results_empty = sum_product([])
results_single = sum_product(test_single_number)

print("Test results:")
print("Sum:", results)
print("Product:", results[1])

print("\nEmpty list test result:", results_empty)
print("\nSingle number test result:", results_single)
```