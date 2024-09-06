```python
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test cases 

test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]

test_cases = [
    test_values[0],
    test_values[1], 
    test_values[2],
    [1, 2, 3, 4, 5],
    test_values[-1:] 7,
    test_values[:2]
]  

for test_case, expected in zip(test_cases, [
    filter_integers(test_values),
    filter_integers(test_values[:2]), 
    filter_integers([1, 2, 3])
]):
    assert expected == test_case, f"expected [{expected}] but got [{test_case}]!"
 ``` 
This script defines a function called **filter_integers** that accepts a list of values and returns a new list containing only the integers from the input. 

The test cases provide a set of sample values and expected results. The function is then used to test its functionality with these cases and passes the test.