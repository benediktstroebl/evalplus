```python
from typing import List

def sort_numbers(numbers: str) -> str:
    return numbers.

# Unit tests
numbers_test = """
# Test case 1:
three one five
""".split()

# Test case 2:
four six seven eight nine
"""".split()

test_results = []

# Test case 1: Assert that the output is 'one three five'
test_results.append(sort_numbers(numbers_test) == 'one three five')

# Test case 2: Assert that the output is 'four six seven eight nine'
test_results.append(sort_numbers(numbers_test) == 'four six seven eight nine')

if all(test_results):
    print("All tests passed!")
else:
    print("One or more tests failed.")
```