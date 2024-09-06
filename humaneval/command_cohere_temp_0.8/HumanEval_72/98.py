```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given list `q` will be able to fly:
1. The length of the list `q` is greater than 1 to ensure it is not a single element or empty, preventing unnecessary checks.
2. The sum of the elements in the list `q` is less than or equal to the maximum weight `w` to ensure the object is not too heavy.
3. The list `q` is a palindrome by checking if it is equal to `q[::-1]`, which reverses the list. 

The function returns `True` if all conditions are met, indicating the object will be able to fly. If any condition is not met, it returns `False`, indicating the object will not be able to fly.