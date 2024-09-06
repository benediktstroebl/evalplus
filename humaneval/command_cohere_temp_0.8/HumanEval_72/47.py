```python
def will_it_fly(q, w):
    return (len(q) > 1 and 
            sum(q) <= w and 
            q == q[::-1])
```

The provided function `will_it_fly` uses three conditional checks to determine if the given list `q` will be able to fly:
1. The length of the list must be greater than 1 to avoid empty lists or single-element lists that cannot be palindromic.
2. The sum of the elements in the list must be less than or equal to the maximum weight `w` to ensure the payload is within the weight restrictions.
3. The list must be a palindrome, meaning it is equal to its reversed version `q[::-1]`.

Each conditional check ensures a necessary condition for the object to be considered flyable. If all conditions are met, the function returns `True`; otherwise, it returns `False`.