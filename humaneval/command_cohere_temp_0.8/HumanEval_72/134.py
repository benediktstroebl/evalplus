```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional statements to determine if the object `q` will be able to fly. 

First, it checks if the object is not a list of length 1, using the condition `len(q) > 1`. This condition ensures that the list is longer than 1, meaning it has multiple elements. 

Following, it checks if the sum of the elements in the list `q` is less than or equal to the maximum weight `w` using the condition `sum(q) <= w`. This part ensures that the weight of the object is less than or equal to the maximum weight it can possibly have. 

Finally, the function checks if the list `q` is a palindrome, meaning it is equal to its reversed version `q[::-1]`. If all conditions are true, the function returns `True`; otherwise, it returns `False`. 

This logic assures that the function `will_it_fly` accurately determines if the object can fly under the provided conditions.