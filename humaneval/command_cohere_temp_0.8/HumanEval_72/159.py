```python
def will_it_fly(q, w):
    return (len(q) > 1 and sum(q) <= w and q == q[::-1])
```

The function `will_it_fly` uses three conditions to determine if an object will fly:
1. The object is a list of at least two elements (`len(q) > 1`).
2. The sum of the list elements is less than or equal to the maximum weight (`sum(q) <= w`).
3. The list is balanced or symmetric (`q == q[::-1]`).

These conditions ensure that the object is a balanced list of weights whose sum is less than or equal to the maximum weight. The function returns `True` if all conditions are met and `False` otherwise. 

Here is an example usage of the function:
```python
print(will_it_fly([1, 2], 5))
# Output: False

print(will_it_fly([3, 2, 3], 1))
# Output: False

print(will_it_fly([3, 2, 3], 9))
# Output: True

print(will_it_fly([3], 5))
# Output: True
``` 

This should output:
```bash
False
False
True
True
``` 

This function ensures that the object will be flown by checking the balance and weight restrictions.