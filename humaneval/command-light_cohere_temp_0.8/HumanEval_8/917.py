Here's the self-contained Python function along with test cases: 

```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Compute the sum and product of a list of integers 
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test cases
test_cases = [
    [], (0, 1)  # Empty sum should be 0 and empty product should be 1
    [1, 2, 3], (10, 24)
]

# Function call and tests
for case in test_cases:
    result = sum_product(case)
    print(f"Case {case} -> {result}")
    assert result == case
```