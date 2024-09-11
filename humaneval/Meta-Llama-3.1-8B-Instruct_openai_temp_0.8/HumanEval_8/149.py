```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in the list.
    """
    # Use built-in functions sum() and math.prod() to calculate sum and product respectively
    # The lambda function used here with map() ensures nothing is passed when list is empty and hence defaults to 1 for product and 0 for sum and then a tuple is returned
    from math import prod as product
    return (sum(numbers) if numbers else 0, product(numbers) if numbers else 1)


# Example usage
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```

However, without using the math library for better understanding and easier implementation in more basic conditions.

```python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        Tuple[int, int]: A tuple consisting of a sum and a product of all the integers in the list.
    """
    sum_nums = 0  # Initialize sum
    product_nums = 1  # Initialize product

    # Iterate over the list to calculate sum and product
    for num in numbers:
        sum_nums += num
        product_nums *= num

    # Return a tuple
    return (sum_nums, product_nums)


# Example usage
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
```