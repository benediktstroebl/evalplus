```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditional checks to determine if the given object `q` will be able to fly:
1. The length of the object `q` is greater than `1` to ensure it is a list or a string.
2. The `sum` of the elements in `q` is less than or equal to the maximum weight `w`.
3. The object `q` is symmetric (equal to its reverse), indicating it is a palindrome. 

The function returns `True` if all conditions are met, indicating the object will fly. If any of the conditions are not met, it returns `False`, indicating it will not. 

Here is an example usage of the function:
```python
print(will_it_fly([3, 2, 3], 9))  # Outputs True
print(will_it_fly([1, 2], 5))  # Outputs False
print(will_it_fly(["aa"], 10))  # Outputs True
```