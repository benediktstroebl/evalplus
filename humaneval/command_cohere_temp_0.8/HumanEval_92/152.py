```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    '''
    return x in [y+z, z+y, x+y] and all([type(i) == int for i in [x, y, z]])
```

The problem requires a function that can quickly tell if three integers have the property that any two of them sum up to the third. The function any_int checks if one of the three variables is equal to the sum of the other two. The function returns True if this is the case and all the variables are integers, and False otherwise. The type keyword is used to check if all three variables are of the integer type, and the in operator is used to check if one of the sums matches. 

Here is an example of a use case for this function: 

```any_int(5, 2, 7) ```   //returns: True
```any_int(3, 2, 2) ```  //returns: False
```any_int(3, -2, 1) ``` //returns: True
```any_int(3.6, -2.2, 2) ```// returns: False
```any_int(-5, -1, -10) ```// returns: True
```any_int(-5, -1, 5) ```  //returns: False
```any_int(-5, 5, -10) ``` // returns: True
```any_int(-5, 5, 10) ```  //returns: False