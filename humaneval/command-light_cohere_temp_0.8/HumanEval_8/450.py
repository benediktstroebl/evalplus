```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
#Test case #1
test_case1 = [1, 2, 3, 4]
result1 = sum_product(test_case1)
print("Test case 1 sum:", result1[0])
print("Test case 1 product:", result1[1])
#Test case #2
test_case2 = []
result2 = sum_product(test_case2)
print("Test case 2 sum:", result2[0])
print("Test case 2 product:", result2[1])
``` 
The function 'sum_product' is self-contained, and its purpose is to produce a tuple with the sum and product of all integers in the list. The function runs through a loop and accumulates the sum and product of integers in the list, testing to see if the output is correct.