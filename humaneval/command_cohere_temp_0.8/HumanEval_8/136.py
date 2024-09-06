```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return (0, 1)
    return (sum(numbers), sum(x * y for x, y in zip(numbers, numbers[1:])) if len(numbers) > 1 else numbers[0])
```

The function works as follows:
- The base case is a list with no elements — it returns `(0, 1)` according to the problem statement. 
- In any other case, it calculates the sum of the list using the built-in `sum` function. 
- To calculate the product, the function iterates over pairs of elements in the list using `zip`, and multiplies them using the `sum` function again. If the list has only one element, it returns the value of that element. 
- Finally, the function returns a tuple with the calculated sum and product. 

This approach provides a solution that is both efficient and readable. I hope this solution suits your needs; please let me know if you have any further questions or if you'd like assistance with anything else!