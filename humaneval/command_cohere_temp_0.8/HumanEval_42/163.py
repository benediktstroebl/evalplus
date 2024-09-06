```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
``` 

This Python script defines a function called `incr_list`. This function takes a list argument and returns a new list in which each element from the input list has been incremented by 1. It uses a list comprehension with the expression `[x + 1 for x in l]` to produce a new list where each element from the input list `l` is incremented by 1. The result is then returned as the output. 

The script passes the provided tests, as it successfully increments each element in the input list and returns the result as a new list. 
```python
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
```