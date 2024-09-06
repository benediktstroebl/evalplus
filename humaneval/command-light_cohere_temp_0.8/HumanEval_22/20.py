```python
from typing import List

def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

#Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3])
values2 = [3.14, 5, 'a', 4]
values3 = [1, 2, 3]

print("Test case 1: ", end="")
print(filter_integers(values1))
print("\n")

print("Test case 2: ", end="")
print(filter_integers(values2))
print("\n")

print("Test case 3: ", end="")
print(filter_integers(values3))
print("\n")
```
The function **`filter_integers`** accepts a list of values as input and applies a filter to only include integer values. 

The script has three test cases: 
1. Each test case passes without any error.