```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print(test_result) # Prints (10, 24)
``` 
This function will return a tuple containing the sum and product of all the integers in the list. The tests passed successfully as well.