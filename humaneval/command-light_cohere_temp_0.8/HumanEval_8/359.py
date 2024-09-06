```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in the list.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Test cases
numbers1 = [1, 2, 3, 4]
result1 = sum_product(numbers1)
print("Test 1 result:", result1)  

numbers2 = []
result2 = sum_product(numbers2)
print("Test 2 result:", result2)

numbers3 = [10, 20, 30]
result3 = sum_product(numbers3)
print("Test 3 result:", result3)

numbers4 = [10, 2, 30]
result4 = sum_product(numbers4)
print("Test 4 result:", result4)
```

This Python script defines a function `sum_product` that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The script also provides several test cases to verify the correctness of the `sum_product` function.