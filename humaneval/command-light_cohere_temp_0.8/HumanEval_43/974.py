```python
def pairs_sum_to_zero(l):
    if not set(l) or len(l) < 2:
        return False
    for i in l:
        for j in l:
            if i + j <= 0:
                return False
    return True

# Test the function
test_result = pairs_sum_to_zero([1, 3, -2, 1, 2, 3, 7])
print("The test result is:", test_result)
```

This Python function, `pairs_sum_to_zero`, takes a list of integers as input and returns `True` if there are two distinct elements in the list whose sum is less than or equal to zero, and `False` otherwise. The function uses a simple techniques to check for the desired property in the input list. 

This function is self-contained, meaning it can be called and does not require any additional functions or data to be used.