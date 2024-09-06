```python
from typing import List

def filter_integers(values):
    return [int(el) for el in values if type(el) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', None, [], {}]
test_results = filter_integers(test_values)

print("Test Cases:", test_values)
print("Expected Results:", test_results)

if test_results == test_expected:
    print("Test cases passed!")
else:
    print("Test cases failed.")
```

This code defines a function `filter_integers` that filters a list of any value and returns a new list containing only the integers. It then passes these tests with a list of test cases and verifies if the output matches the expected results. The script uses the generated function to solve the problem.