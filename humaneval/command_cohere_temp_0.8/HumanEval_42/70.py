Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This script defines a function called `incr_list` that takes a list argument and returns a new list with its elements incremented by 1. The function uses a list comprehension to iterate over each element in the input list and adds 1 to it. The result is then returned as the output.

To verify the functionality of the script, you can test it using the following markdown code block:
```python
tested = [1, 2, 3, 5, 3, 5, 2, 3, 9, 0, 123]
assert incr_list(tested) == [2, 3, 4, 6, 4, 6, 3, 4, 10, 1, 124]
``` 
The asserted output corresponds to the element-wise incrementation by 1 of the original list in the argument.

The provided code snippet solves the problem and passes the tests without explicitly defining a main function or an external test suite, making it a self-contained solution to the problem. 
If you wish to test the function on other input lists, you can call `incr_list()` with the list of your choice, and it will return the incremented list. 

Let me know if you would like me to provide an explanation of any part of the code or clarify any other aspects related to the problem at hand! I am grateful to assist you in understanding these concepts, and please let me know if you want to dive deeper into any specific topic!