```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    a = x + y
    b = y + z
    c = x + z
    
    if a == int(a) and b == int(b) and c == int(c) and (a == b or a == c or b == c):
        return True
    else:
        return False
```

This function evaluates the conditions required for the truth value 'True' explicitly. It performs the necessary calculations by summing all possible pairs of the three numbers provided. It also ensures that the condition requiring integers is fulfilled by applying the int() function and comparing the results. Finally, it checks if any of the sums are equal and returns 'True' if any of them are. Otherwise, it returns 'False'. 

The function is self-contained and does not rely on any external variables or functions. It is written to be concise and specific to the problem at hand. 

To test this function, one can run an unit test suite containing a variety of test cases like the ones provided in the problem statement, to ensure its correctness.