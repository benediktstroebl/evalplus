Here's a self-contained Python script with a function that filters out integers from a list of various types:
```python
from typing import List, Any

def filter_integers(values:
    # Filtering for only integers
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    [],  # [] contains no integers
    ['a', 3, 'c'],
    [1, 2, '3'],
    [1, 2, 3],
    [5, '6'],
    [1, 2, 3, 4, '5'],
]

results = []
for test_data in test_cases:
    # Function call
    filtered_ints = filter_integers(test_data)
    results.append(filtered_ints)

# Print results
for result, expected in zip(results, test_cases[0]):
    print(f'Expected: { {expected}, } but was {result}.'), '\n')
```
This script defines a function **filter_integers** that filters out integers from a given list. It uses the ** typing** module to ensure type-checking. 

The script includes a list of test cases, which are passed to the function for filtering. The function then returns a filtered list of integers. 

The results are compared with the expected output from each test case and printed to the console.