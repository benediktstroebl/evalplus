Here is a Python script that contains a self-contained function that filters out integers from a given list:
```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if isinstance(x, int)]

# Test the function with a few inputs and checks for expected outputs
test_filter_integers = []
test_filter_integers.append([1, 2, 3])
test_filter_integers.append([4, 'abc'])
test_filter_integers.append([1, 2, 3, 4])
test_filter_integers.append([1, 2, 3, 'a'])
test_filter_integers.append([1, 2, 3, 4, 5])

# Run the function and compare the outputs with the expected results
assert list(filter_integers(test_filter_integers)) == [1, 2, 3]

print("Test filtering integers: ", end='')
for expected, actual in zip(test_filter_integers, filter_integers(test_filter_integers)):
    print(expected, end=' ')
print()
```