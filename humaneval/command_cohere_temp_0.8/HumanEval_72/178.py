```python
def will_it_fly(q, w):
    return (q == q[::-1] and sum(q) <= w)
```

This function will return True if the object q will fly, and False otherwise. The object q will fly if it is balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w. The function works by first comparing the list q to its reversed version using the condition q == q[::-1]. If the list is balanced, it will return True. Otherwise, it will return False. The function will also check if the sum of the elements of q is less than or equal the maximum possible weight w using the condition sum(q) <= w. If the condition is true, it will return True. Otherwise, it will return False. 

Here is an example of how to use this function:
```python
print(will_it_fly([1, 2], 5))  # Output: False
print(will_it_fly([3, 2, 3], 1))  # Output: False
print(will_it_fly([3, 2, 3], 9))  # Output: True
print(will_it_fly([3], 5))  # Output: True
``` 
This function will return the correct value for each test case.