Here's a Python script with a self-contained function that solves the problem:
```python
def incr_list(l: list):
    result = [x + 1 for x in l]
    return result
```
This function takes a list as input and returns a new list with each element incremented by 1. It uses a list comprehension to iterate over each element in the input list and adds 1 to it, effectively incrementing it. The function is self-contained and can easily be copied and pasted into a Python environment to test it out. 

Here is an example of how you can use the `incr_list` function to increment the list `[1, 2, 3]`:
```python
result = incr_list([1, 2, 3])
print(result)  # Output: [2, 3, 4]
```
You can also test the function with complex test cases to ensure its correctness. For example:
```python
>>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
[6, 4, 6, 3, 4, 4, 10, 1, 124]
``` 
This demonstrates that the `incr_list` function correctly increments each element in the list by 1. 
Let me know if I can assist with anything else!