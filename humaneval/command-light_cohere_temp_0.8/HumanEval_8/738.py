```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Each number is only once in the product.
    Calculate the result with type hints.
    """
    def calculate_sum_product(list_of_numbers: List[int]) -> Tuple[int, int]:
        return (sum(list_of_numbers), product(list_of_numbers))
    return calculate_sum_product(numbers)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    result = calculate_sum_product(numbers)
    print(f"Sum: {result[0]}, Product: {result[1]}")
```