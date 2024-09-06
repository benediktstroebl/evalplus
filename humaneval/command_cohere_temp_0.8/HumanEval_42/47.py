Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function `incr_list` takes a list as an argument and returns a list where each element is incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it. 

To test this function, you can run the following code:
```python
Test incr_list()
>> incr_list([1, 2, 3])
[2, 3, 4]
>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The expected output of testing the given examples is returned. 

This function solves the problem and passes the tests without relying on any external variables, and it provides a clear and efficient solution. 
If you would like, we can provide more examples of how the function can be applied.  different use cases, and we can discuss optimizations or alternative approaches if desired.