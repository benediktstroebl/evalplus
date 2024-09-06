Here's a Python script with a self-contained function that solves the problem:
```python
def get_positive(l):
    return [x for x in l if x > 0]
```
This function uses a list comprehension, which is a short way of writing a for loop, to create a new list `x` containing only the positive numbers from the input list `l`. The expression `x for x in l if x > 0` creates a new list or sequence, where each element `x` in the input list `l` is included only if it is greater than `0`. 

You can use this like any other Python function and test it with different input lists to verify that it works as described. For example:
```python
print(get_positive([-1, 2, -4, 5, 6])) # [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) # [5, 3, 2, 3, 9, 123, 1]
```
This function is straightforward and easy to use. It also has TDD-friendly syntax, making it easy to test and confirm that the output matches the expected result. 
You can use this function in other parts of your code or even distribute it as a separate module, and other developers can use it as well. H appended to the function.