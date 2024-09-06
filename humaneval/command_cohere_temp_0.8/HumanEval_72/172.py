```python
def will_it_fly(q, w):
    return (len(q) == 1 or len(q) == 2 and q[0] == q[1]) and sum(q) <= w
```
The function will return True if the object q will be able to fly and False otherwise. It checks if the list is palindromic and the sum of the object sum is less than or equal to the maximum possible weight. The function will return the desired result for the provided examples in the prompt.