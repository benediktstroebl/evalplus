```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses two conditions to determine if an object will fly:
1. The object is considered balanced if it is a list with a length of 1 or if it is a palindromic list. This is determined by checking if the list `q` has a length of 1 or if it is equal to its reversed counterpart (`q[::-1]`).
2. The total weight of the object is less than or equal to the specified maximum weight `w`. This is determined by using the `sum` function to add up the elements in the list `q`.

The function returns `True` if both conditions are met, and `False` otherwise. 

#### Example Usage:
```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
```

This script will yield the following outputs:
```bash
False
False
True
True
```