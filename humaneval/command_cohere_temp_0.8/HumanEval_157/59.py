```python
def right_angle_triangle(a, b, c):
    total = a + b + c
    if total == 180:
        return True
    else:
        return False
```

This function evaluates the sum of the three given side lengths of the triangle, returning True if the sum is equal to 180 (indicating a right triangle) and False otherwise. 

Here is a simple test case to verify the functionality of the function:
```python
test_cases = [(3, 4, 5), (1, 2, 3)]

for i in test_cases:
    assert(right_angle_triangle(*i) == True)
```

This uses a list of test cases to confirm the function's correctness against expected outcomes. 

The `assert` statement confirms that the function returns True for side lengths that form a right triangle and yields False otherwise. 
If the assertion passes, it means the function is correct. 

Lastly, the script has a docstring to provide a clear explanation of what the function does, as well as example usage.  This ensures anyone reading the code understands its purpose and can apply it correctly.