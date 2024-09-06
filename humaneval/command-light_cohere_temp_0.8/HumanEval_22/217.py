```python
from typing import List

def filter_integers(values:
    """
    filtered_ints = []
    for value in values:
        if isinstance(value, (int, float)):
            filtered_ints.append(value)
    filtered_ints
    return filtered_ints

# unit test
test_filter = []
test_filter.push_str("int")
test_filter.push(3)
test_filter.push_str("abc")
test_filter.push(1.14)
test_filter.push(5)
test_filter.push(None)
test_filter.push(True)
test_filter = filter_integers(test_filter)
test_filter = [3, 5,1.10,float('3.14'),None]
print(test_filter)
``` 
This Python script defines a function `filter_integers` that filters a list of values based on whether each element is an integer. The function iterates through a list of any values and checks if each element is an instance of either `int` or `float`, and if so, it is added to a new list that will be returned. The script also includes a unit test that adds a variety of values to the `test_filter` list and then calls the `filter_integers` function to see if it returns the correct result.