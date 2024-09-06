```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    result = numbers[0] * numbers[1] + sum_product(numbers[1:])
    return (result, result * numbers[0])

# Unit tests
test_sum_product = [
    dict(
        zip(
            ["1", 2, 3, 4",],
            [(), 1, 24, 120]
        )
    )

test_sum_product_empty = []

if __name__ == "__main__":
    assert sum_product(test_sum_product) == (1, 1)
    assert sum_product(test_sum_product_empty) == (0, 1)
    print("All tests passed!")
```

This script defines a function called sum_product that takes a list of integers and returns a tuple with the sum and product of the numbers. The function also has unit tests that check the correctness of the function. The tests pass when the print statements.