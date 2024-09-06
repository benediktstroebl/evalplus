```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional statements to check if the passed object `q` will be able to fly. The conditions are:
1. The object `q` should be a list of size greater than 1. This ensures that we are dealing with a "real" object and not just a single element, which cannot be balanced.
2. The sum of the elements in the list `q` should be less than or equal to the maximum weight `w`. This ensures that the total weight of the object is within the acceptable range.
3. The list `q` is symmetric, meaning it's equal to its reverse iteration `q[::-1]`. This determines if the list is balanced or not. 

All these conditions need to be fulfilled for the function to return `True`, otherwise, it returns `False`.  This problem can be solved using a single boolean logic statement, as shown in the code above.