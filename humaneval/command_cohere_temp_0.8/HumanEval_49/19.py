Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which calculates 2^n modulo p, where n and p are integer arguments. It uses the built-in pow function to accomplish this calculation. 
Since the problem states that the function 'modp' should return the result as an integer (not an integer object), there is no need for an explicit cast to int, and the function result will already be returned as an integer value. 
To test this function, you can call it with different input values and verify that it returns the expected results based on the problem description. Here is an example:
```python
# Testing the modp function
assert modp(3, 5) == 3
assert modp(1101, 101) == 2
assert modp(0, 101) == 1
assert modp(3, 11) == 8
assert modp(100, 101) == 1
```

This block of code tests the defined function modp using Python's assert statement, which checks whether the expression's two arguments have the same value, and if the assertion fails, it raises an AssertionError exception. If the values are equal, the assertion passes and does not raise any error. 

Finally, the function is defined and tested, making this script a self-contained solution to the problem.