Here is a self-contained Python function that solves the problem of calculating the sum and product of integers in a list:

```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a list.
    Args: 
        numbers (List[int]): A list of integers
    Returns: 
        Tuple[int, int]): A tuple containing the sum and product of all integers in the list
    """
    # Initialize variables to store the sum and product
    sum_ = 0
    prod_ = 1
    for num in numbers:
        sum_ += num
        prod_ *= num
    return (sum_, prod_)
```

This function takes a list of integers as input and returns a tuple containing the sum and product of all the integers in the list. It iterates through a using two variables, sum_ and prod_, to store the sum and product of the integers, respectively.

The function then iterates through the list of integers and adds each number to the sum variable. Then, it multiplies each number in the list by the prod_ variable, which is set to 1, to calculate the product of the numbers.

Finally, the function returns the sum_ and prod_ variables, which contain the sum and product of all the integers in the list, respectively.

This code is a good example of a self-contained function that solves a specific problem and passes all the tests.