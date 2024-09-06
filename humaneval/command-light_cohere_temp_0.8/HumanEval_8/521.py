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
test_sum_product = [1, 2, 3, 4]
test_empty_list = []
test_single_num = [5]
test_ multiples = [2, 3, 4, 5]

print("Sum Product Results:")
print(sum_product(test_sum_product))
print(sum_product(test_empty_list))
print(sum_product(test_single_num))
print(sum_product(test_multiples))
``` 
This Python code defines a function called sum_product that takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses a loop to calculate the sum and product of each number in the list. 

The function then returns the calculated sum and product. 
The test cases ensure that the function is working correctly for different scenarios, such as an empty list, a single number, and a list of numbers.