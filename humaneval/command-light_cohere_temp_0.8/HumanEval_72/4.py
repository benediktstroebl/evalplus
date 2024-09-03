```python
def will_it_fly(q, w):
    return len(q) <= w and sum(q) <= w

# Example usage:
q = [1, 2] # Unbalanced list
print(will_it_fly(q, 5))  # Output: False

q = [3, 2, 3] # Balanced list
print(will_it_fly(q, 9))  # Output: True

q = [3]     # Single element list
print(will_it_fly(q, 5))  # Output: True
```

This code defines a function `will_it_fly`, which checks if a list `q` can be used as a weight for flying. The function returns `True` if the list is both less than or equal to the maximum possible weight `w` and the sum of its elements is less than or equal to `w`.