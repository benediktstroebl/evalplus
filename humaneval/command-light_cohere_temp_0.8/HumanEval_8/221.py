```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Create list with values
my_list = [1, 2, 3, 4, 5]
# Call function and print results
print(sum_product(my_list))
``` 
The above Python script defines a function called sum_product, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers in the list. The function uses two variables, sum and product, to iterate through the list and calculate the sum and product, respectively. The sum is calculated by adding each integer in the list, and the product is calculated by multiplying each integer in the list. The product is then initialized to 1 and then multiplied by each integer in the list.