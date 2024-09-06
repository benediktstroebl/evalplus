Here is a Python script that defines a function, `filter_integers`, which filters a list of any Python values and returns a new list containing only the integers:
```python
from typing import List

def filter_integers(values:
    # Filter list for only integers and return
    return [x for x in values if isinstance(x, int)]

# Test cases
test_cases = [
    ['a', 3.14, 5],
    [1, 2, 3, 'abc', {}, []],
]

# Function call and print results
print(filter_integers(test_cases))
```

The script is designed to solve the problem of filtering a list of any Python values and return a new list containing only the integers. The `filter_integers` function takes a list of any Python values (`values`) as an argument and returns a new list containing only the integers from the `values` list. The function uses the test case to ensure that the function is called correctly and that the input is valid. The test case defines a list of test cases, and the `filter_integers` function is called with the `test_cases` list as an argument. The function then returns the result, and the print statement prints the result to the console.