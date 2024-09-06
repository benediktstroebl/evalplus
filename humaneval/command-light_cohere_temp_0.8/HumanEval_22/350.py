Here is a self-contained Python function that filters integers from a given list:
```python
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1 result:", filter_integers(values1))
print("Test case 2 result:", filter_integers(values2))
```
The code defines a function `filter_integers` that accepts a list of values as an argument. The function uses a filtering process to return a new list that includes only the elements that are integers. It utilizes the Python's `isinstance()` function to check if each element in the input list is an instance of the built-in `int` class. 

The code then provides two test cases, `values1` and `values2`, which have lists of different values. The `filter_integers` function is called with these test cases, and the results are printed to the console. This shows that the filter function correctly filters out non-integer elements from the input lists and returns a new list with only the integers.