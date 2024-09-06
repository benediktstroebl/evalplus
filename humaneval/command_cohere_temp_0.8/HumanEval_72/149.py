```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The function will return True if the object `q` will fly according to the given criteria, and False otherwise. The criteria are:
- The object `q` is a list with more than one element `len(q) > 1`.
- The sum of the elements in `q` is less than or equal to the maximum possible weight `sum(q) <= w`.
- The list `q` is palindromic, i.e., it is equal to its reversed version `q == q[::-1]`. 

Examples of lists that would return True include `[3, 2, 3]` with a maximum weight of 9, and `[3]` with a maximum weight of 5. An example of a list that would return False is `[1, 2]` with a maximum weight of 5, since while it is palindic and the sum of its elements is less than the maximum weight, it does not have multiple elements.