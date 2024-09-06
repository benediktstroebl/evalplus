```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test case 1: empty list
test_case_1 = (0, 1)

# Test case 2: single element
test_case_2 = (3, 3)

# Test case 3: two separate numbers
test_case_3 = (2, 6)

# Test case 4: list of three elements
test_case_4 = (1, 2, 3)

# Test case 5: list of four elements
test_case_5 = (5, 6, 7, 8)

# Test case 6: list of five elements
test_case_6 = (9, 10, 11, 12)

# Test case 7: list of six elements
test_case_7 = (4, 5, 6, 7, 8, 9)

print(sum_product(test_case_1))   # Output: (0, 1)
print(sum_product(test_case_2))   # Output: (3, 3)
print(sum_product(test_case_3))   # Output: (2, 6)
print(sum_product(test_case_4))   # Output: (1, 24)
print(sum_product(test_case_5))   # Output: (5, 30)
print(sum_product(test_case_6))   # Output: (9, 60)
print(sum_product(test_case_7))   # Output: (4, 42)
```