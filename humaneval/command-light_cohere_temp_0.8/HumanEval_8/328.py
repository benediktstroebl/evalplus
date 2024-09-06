```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in the list.
    if not numbers:  # empty list
        return (0, 1)
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("Input list must only contain integers")
    return sum(numbers), product(numbers)
    return (sum(numbers), sum(numbers) * product(numbers))

tests = [
    input(" passing test cases...")
    test_sum_product_func = sum_product

    test_sum_product_func([1, 2, 3, 4]))
    assert test_sum_product_func[0] == 10
    assert test_sum_product_func[1] == 24

    test_sum_product_func([])
    assert test_sum_product_func[0] == 0
    assert test_sum_product_func[1] == 1

    test_sum_product_func([1, 2, 3, 4], 5))
    assert test_sum_product_func[0] == 10
    assert test_sum_product_func[1] == 25

    test_sum_product_func([1, 2, 3])
    assert test_sum_product_func[0] == 6
    assert test_sum_product_func[1] == 12

    test_sum_product_func([10, 20, 30])
    assert test_sum_product_func[0] == 60
    assert test_sum_product_func[1] == 120

    test_sum_product_func([10, 20, 30], 40)
    assert test_sum_product_func[0] == 60
    assert test_sum_product_func[1] == 240

    test_sum_product_func([10, 20, 30, 40, 50])
    assert test_sum_product_func[0] == 120
    assert test_sum_product_func[1] == 300

    test_sum_product_func([10, 20, 30, 40, 50], 60)
    assert test_sum_product_func[0] == 120
    assert test_sum_product_func[1] == 360
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function follows the template to handle different scenarios: empty list, non-integer elements, or valid input. The tests ensure that function works correctly with different inputs.