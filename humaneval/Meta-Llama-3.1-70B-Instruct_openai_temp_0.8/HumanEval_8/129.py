```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    :param numbers: A list of integers
    :return: A tuple of two integers, sum and product of all the integers in the list
    """
    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 0, 1]))  # Expected output: (0, 0)
print(sum_product([5]))  # Expected output: (5, 5)
print(sum_product([]))  # Expected output: (0, 1)
```

However, the total_product isn't quite correct in the above code. For an empty list, we should get 1 for product (As per mathematical rule that product of no numbers is 1). The above code works fine as long as there is at least one number in the list. But we should explicitly handle the case when list is empty.

Here is the corrected version:

```python
from typing import List, Tuple
import math

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    :param numbers: A list of integers
    :return: A tuple of two integers, sum and product of all the integers in the list
    """
    total_sum = sum(numbers)
    
    # Using math.prod to calculate product of all numbers in the list
    # math.prod returns 1 for empty list
    total_product = math.prod(numbers, start=1)
    
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 0, 1]))  # Expected output: (0, 0)
print(sum_product([5]))  # Expected output: (5, 5)
```

Please note that `math.prod` was added to Python in version 3.8. If you're using an earlier version, you can calculate the product manually:

```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    
    :param numbers: A list of integers
    :return: A tuple of two integers, sum and product of all the integers in the list
    """
    total_sum = sum(numbers)
    total_product = 1
    for number in numbers:
        total_product *= number
    
    # If list is empty, total_product will still be 1
    return total_sum, total_product

# Test cases
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, 0, 1]))  # Expected output: (0, 0