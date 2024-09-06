```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine whether the given list `q` will fly with a maximum weight of `w`:
1. The length of the list `q` is greater than 1 to ensure it is not a single element or empty, ensuring it is a valid object to consider for flight.
2. The sum of the elements in list `q` is less than or equal to the maximum weight `w` to ensure the object will not exceed the weight capacity.
3. Palindromic nature is checked by comparing the list `q` with its reverse `(q[::-1])`, ensuring it is balanced. 

Returning `True` if all conditions are met, the object will fly; otherwise, it returns `False`.