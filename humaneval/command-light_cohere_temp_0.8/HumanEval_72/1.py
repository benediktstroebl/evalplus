```python
def will_it_fly(q, w):
    return q.is_palindrome(w) and sum(q) <= w
 
# Example usage:
q = [3, 2, 3]
w = 9
print(will_it_fly(q, w))  # True
```
This Python function `will_it_fly` takes a list `q` and a maximum weight `w` as parameters. It uses the fact to check if the list is a palindrome and whether its sum is less than or equal to the maximum weight `w`. If both conditions are met, the function returns `True`, indicating that the list will fly. If not, it returns `False`. 

The function is well-contained and provides a straightforward way to determine whether the given list will be able to fly based on the maximum weight.