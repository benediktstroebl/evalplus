```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine whether the given list `q` will fly with a maximum weight of `w`:
1. The length of the list `q` is greater than 1 to ensure it is not a single element or empty, ensuring it is a valid object to consider for flight.
2. The sum of the elements in list `q` is less than or equal to the maximum weight `w`, ensuring the object will not exceed the weight capacity.
3. Palindromic nature is checked by comparing the list `q` with its reverse (`q[::-1]`) to verify if it is balanced. 

Combining these conditions assures that the function returns `True` only when the list is both palindromic and its sum matches the weight constraint.