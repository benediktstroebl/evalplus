```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
``` 

This Python script defines a function called `incr_list` that takes a list `l` as input. Inside the function, it uses a list comprehension to iterate over each element `x` in the input list `l`, and for each element, it adds 1 to it using the `+ 1` operation. These modified elements are collected in the `result` list. 

The function then returns the `result` list, which contains the input list's elements incremented by 1. 

The script ensures that the function works correctly and produces the expected output for various input lists, as depicted in the problem statement.  The purity of the function is also maintained as desired.