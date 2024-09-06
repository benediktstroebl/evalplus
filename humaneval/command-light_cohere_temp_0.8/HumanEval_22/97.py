Here is a Python script that defines a function called filter_integers, which takes a list of values and returns a new list containing only the integers from the input:
```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_data = [1, 2, 3, 'abc', 4, 'cva', {}]
test_cases = [filter_integers(test_data), lambda x: isinstance(x, int)]
print(test_cases)
```
The output of this script will be a list of lists, where each inner list contains integers only. This demonstrates a the test to filter out non-integer values from a given list. 

The test_cases lambda function creates a list of values and passes it to the function as an argument, and the function returns a new list with only the integers from the original list.