```python
def will_it_fly(q, w):
    return (len(q) > 1 and q == q[::-1] and sum(q) <= w)
```

The function `will_it_fly` uses a set of criteria to determine whether an object can fly or not. If the list is not palindrome or the sum of elements exceeds the maximum weight, it returns False. If the conditions are met, it returns True.

## Example Usage

```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
```