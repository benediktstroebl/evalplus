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
test_case_1 = sum_product([])
print("Test case 1: Empty list, sum =", test_case_1)

# Test case 2: Single number list
test_case_2 = sum_product([1])
print("Test case 2:", test_case_2)

# Test case 3: Longer list
test_case_3 = sum_product([1, 2, 3, 4, 5])
print("Test case 3: sum =", test_case_3)

# Test case 4: Reversed list
test_case_4 = sum_product([4, 5, 3, 2, 1])
print("Test case 4: sum =", test_case_4)
``` 
This code provides a function `sum_product` that takes a list of integers and returns a tuple with the sum and product of the numbers in the list. It is then pass four tests to validate the functionality of the function.