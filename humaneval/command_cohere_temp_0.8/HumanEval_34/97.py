```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements from l. The function uses the built-in Python set to automatically remove duplicate elements, and then uses the sort() method to sort the elements. 

To ensure the function adheres to the problem statement, you can unit test the function using the following code, which verifies the output against a known output for a specific input:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
expected_result = [0, 2, 3, 5, 9, 123]

assert unique(test_list) == expected_result
``` 
This will verify that the unique function behaves as expected, sorting and removing duplicates from the input list.