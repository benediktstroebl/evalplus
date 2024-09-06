```python
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert result_test1 == [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3]
```
This Python script defines a function called **filter_integers** that takes a list of values as an argument and returns a new list that includes only the integer elements from the original list. The test cases provided help to demonstrate the functionality of the function, passing in two sets of values and asserting that the resulting lists contain only integers, which is what the function is expected to produce. 

The function uses a generator expression to create a new list, filtering out any elements that are not integers, and passing those elements to the **List[Any]** argument, which is transformed into a list of integers.