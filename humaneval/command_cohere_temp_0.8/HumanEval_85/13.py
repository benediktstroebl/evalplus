```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This function uses a list comprehension to filter out even integers from the list that are located at odd indices, and then returns their sum. 

Note that the function assumes that the list contains only integers, as the `%` operator is used to determine even or oddness. If the list contains other data types, the function may not provide the expected result. 

If the list lst is empty, the function should handle the edge case and return 0. 

Let's add a unit test to check for this edge case:
```python
def test_add_empty_list():
    assert add([]) == 0
```
Adding this test ensures that the edge case of an empty list is handled properly, and the sum is correctly returned as 0. 

This will result in the following markdown code block:
```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)

def test_add_empty_list():
    assert add([]) == 0
```