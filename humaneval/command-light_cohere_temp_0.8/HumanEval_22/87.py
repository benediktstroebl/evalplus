```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
values_test_case1 = ['a', 3.14, 5]
values_test_case2 = [1, 2, 3, 'abc', {}, []]
print("Test Case 1: ", end="")
print(filter_integers(values_test_case1))
print("\n")

print("Test Case 2: ", end="")
print(filter_integers(values_test_case2))
``` 
This script defines a function **filter_integers** that accepts a list of values as an argument. It uses the specific programming technique to filter out all values from the list except those of type **int** using the Python list comprehension. The script then passes the test cases and prints the output for both test cases.