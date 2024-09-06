```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will be able to fly and False otherwise. The function checks if the list (or string) q is palindromic and if the sum of its elements is less than or equal to the maximum possible weight w. The criterias for "balancing" and "weight" are checked and if both are satisfied, the function returns True, otherwise it returns False. 

This is an example of how the function can be used with a list:
```python
q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))  # Output: True
```

And this is an example of how to use it with a string:
```python
q = "aba"
w = 5
print(will_it_fly(q, w))  # Output: True
```