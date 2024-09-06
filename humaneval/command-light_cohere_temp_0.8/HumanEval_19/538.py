```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(n) for n in numbers.
    return ' '.join(sorted(numbers))

# Unit tests
test_sort_numbers = []
test_numbers = ['three one five', 'two three four', 'zero seven eight', 'one nine six']

# Function call
test_sort_numbers.make()sort_numbers(test_numbers)

# Test case comparisons
for test in test_sort_numbers:
    assert test == ''.join(sorted(test_numbers))
```  This script defines a function **`sort_numbers`** that arranges a space-delimited list of numbers (from 'zero' to 'nine') in ascending order and returns the sorted result as a string. The test case is an list of test numbers, and the function is called with this list. The script then verifies that the function's output for each test case correctly, ensuring the function's correctness.