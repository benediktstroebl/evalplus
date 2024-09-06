```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will fly, and False otherwise. The function checks if the list (or string) q is palindromic and if the sum of its elements is less than or equal the maximum possible weight w. 

Here is an example usage of the function:
```python
print(will_it_fly([3, 2, 3], 9))  # This will print True
print(will_it_fly([1, 2], 5))  # This will print False
``` 

All the test cases provided in the problem statement will yield the correct result using this function.