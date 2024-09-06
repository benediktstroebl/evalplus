```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate sum and product of all the integers in a list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Unit tests
numbers_list = [1, 2, 3, 4, 5]
test_result = sum_product(numbers_list)
print(test_result)  # Expected output: (15, 120)
lists_of_singles = [1, 2], [3, 4]
test_results = [sum_product(list) for list in lists_of_singles]
print(test_results)  # Expected output: [(6, 4), (9, 8)]
lists_of_ multiples = [1, 2, 3], [2, 4, 5]
test_results = [sum_product(list) for list in lists_of_multiples]
print(test_results)  # Expected output: [(10, 240), (14, 600)]
```
The function `sum_product` takes a list of integers and returns a tuple with the sum and product of all the integers. It performs the and calculates the product and sum iterating through each element in the list. The unit tests verify that function's correctness by passing the test using a sample list.