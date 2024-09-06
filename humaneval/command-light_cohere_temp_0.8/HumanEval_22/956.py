```python
def filter_integers(values): 
    """ Filter given list of any python values only for integers."""
    return [num for num in values if isinstance(num, int)]

# Test cases 

# Test case 1
values = ['a', 3.14, 5]
assert filter_integers(values) == [5]

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
assert filter_integers(values) == [1, 2, 3]

# Test case 3
values = [True, False, 3, 4, 5, '6']
assert filter_integers(values) == [3, 4, 5]
``` 
The function **filter_integers** takes a list of values as input and returns a new list containing only the integers from the input list. The function uses a simple for loop to iterate through the input list and check if each element is an instance of the int class. 

Note that this function is self-contained, and it can be used anywhere within a Python program without the need for external functions or modules.