```python
from typing import List
def sort_numbers(numbers: str) -> str:
    numbers = [int(x) for x in numbers.
    return ' '.join(sorted(numbers))

# Basic test cases
test_sort_numbers = []
test_sort_numbers.append(['three, 'one', 'five'])
test_sort_numbers.append(['two', 'zero', 'seven'])
test_sort_numbers.append(['four', 'six', 'eight'])

def test_function():
    return sort_numbers(' '.join(test_sort_numbers))

# Test suite execution
run_tests = []
run_tests.append(test_sort_numbers)
run_tests.append(test_function())
result = run_tests()
print(result)
 ```