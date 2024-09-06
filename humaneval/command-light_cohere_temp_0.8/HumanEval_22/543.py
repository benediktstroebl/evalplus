```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
test_results = [filter_integers(v) for v in test_values]

print(test_results)

``` 
This script defines a function **filter_integers** that takes a list of values and returns a new list with only the integers from the input. It uses a filtering technique on the list comprehension to achieve this.