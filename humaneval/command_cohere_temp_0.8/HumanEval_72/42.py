```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given list `q` will fly with a maximum weight of `w`:
1. The length of the list `q` is greater than 1 to ensure it is not a single element or empty, ensuring it is a valid object for flight.
2. The sum of the elements in list `q` is less than or equal to the maximum weight `w`, ensuring the object's weight is within the allowable limit.
3. The list `q` is symmetric (palindrome) – it is equal to its reversed version `q[::-1]`. This ensures the object is balanced. 

Examples that illustrate when the function returns `True` or `False` are also provided in the original problem statement.