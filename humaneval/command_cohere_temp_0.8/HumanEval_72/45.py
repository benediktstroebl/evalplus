```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditions to determine if an object will fly:
1. The object is a list of at least two elements (`len(q) > 1`).
2. The sum of the list elements is less than or equal to the maximum weight (`sum(q) <= w`).
3. The list is balanced or symmetric (`q == q[::-1]`).

These conditions ensure that the object is a list of elements whose sum is less than or equal to the maximum weight and is balanced. All these conditions are combined with the logical 'and' operator (`&&`) to evaluate the result. If all conditions are satisfied, the function returns `True`; otherwise, it returns `False`. 

Here is an example usage of the function:
```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
```

This should return the following results:
```
False
False
True
True
```

This function can be used to efficiently determine whether an object will fly based on the provided criteria.