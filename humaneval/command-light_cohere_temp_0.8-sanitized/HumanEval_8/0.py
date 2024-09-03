from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:  # zero or empty list
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)