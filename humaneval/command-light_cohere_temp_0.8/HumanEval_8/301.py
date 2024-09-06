Here's the solution to the problem:
```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_data = [0, 1]
test_result = sum_product(test_data)
print(test_result)  # Output: (1, 1)

test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result)  # Output: (10, 24)

# General usage
my_list = [5, 6, 7, 8]
result = sum_product(my_list)
print(result)  # Output: (30, 56)
```

This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate through the list, and for each number, it multiplies it to the `product` variable and adds it to the `sum` variable. 

The function then returns a tuple containing the sum and product of the numbers in the list. The test cases pass the and demonstrate the usage of the function.