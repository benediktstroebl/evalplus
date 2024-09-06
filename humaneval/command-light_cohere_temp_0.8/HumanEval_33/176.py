```python
def sort_third(lst):
    # Sort list by values that are not divisible by three
    return sorted(lst, key=lambda x: not_divisible(x), reverse=True)
    
def not_divisible(x):
    # Check if x is divisible by three
    return x % 3 == 0
```
The function `not_divisible` takes an integer `x` as input and returns `True` if the number is divisible by three, and `False` otherwise. 

The function uses the mathematical modulo operator (`%`) to check if the remainder of `x` divided by `3` is equal to zero. The function returns `True` to pass the test.