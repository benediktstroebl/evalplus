```python
from typing import List
def filter_integers(values): 
    return [i for i in values if type(i) == int]

# Example values for testing
values_test = [['a', 3.14, 5, 1, 2, 'abc', {}, []]

# Test the function
test_result = filter_integers(values_test)
print("Test Result:", test_result)
``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function utilizes a list comprehension to iterate through the values and filter out any non-integer values. 

The script then provides example values for testing and passes those values through the function. Finally, it prints the result to the console, which should be the filtered list of integers. 

I can improve this script by adding more comprehensive tests, handling edge cases, or providing additional informative comments to make it more readable and easier to understand.