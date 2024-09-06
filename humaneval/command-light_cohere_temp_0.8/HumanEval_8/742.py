```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
#Test case 1: empty list
test_case_1 = sum_product([])
print("Test case 1: sum = ",test_case_1)
print("Test case 1: product = ",test_case_1[1])
#Test case 2: list with one element
test_case_2 = sum_product([1])
print("Test case 2: sum = ",test_case_2)
print("Test case 2: product = ",test_case_2[1])
#Test case 3: list with multiple elements
test_case_3 = sum_product([1, 2, 3])
print("Test case 3: sum = ",test_case_3)
print("Test case 3: product = ",test_case_3[1])
```
This code defines the `sum_product` function, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function initializes a product variable to 1 and calculates the sum of the numbers in the list, and then, it multiplies the sum by the product variable to get the product of the numbers in the list.