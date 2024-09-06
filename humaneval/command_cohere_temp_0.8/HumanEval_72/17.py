```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional statements to verify whether the list `q` possesses the following characteristics:
1. The number of elements in the list `q` is greater than 1. This ensures that the list is not empty and consists of more than one element.
2. The sum of the elements in list `q` is less than or equal to the maximum weight `w`. This ensures that the total weight of the object is less than or equal to the maximum possible weight.
3. The list `q` is symmetric (or palindromic), meaning that it is equal to its reversed version `q[::-1]`. 

The function returns `True` if all these conditions are met, and `False` otherwise.  This allows to determine whether the object can fly with the given characteristics.