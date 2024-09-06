```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the list `q` is both palindic (symmetric) and the sum of its elements is less than or equal to the given maximum weight `w`. Otherwise, it returns False. The given examples in the problem statement would return the following results:
```python
will_it_fly([1, 2], 5)  # Returns False 
will_it_fly([3, 2, 3], 1)  # Returns False
will_it_fly([3, 2, 3], 9)  # Returns True
will_it_fly([3], 5)  # Returns True
``` 

This is a logical function that relies on two fundamental criteria: the symmetry of the list and the relative size of the sum of its elements to the given weight. If both conditions are met, the function returns True, signifying that the object can fly under the given constraints.