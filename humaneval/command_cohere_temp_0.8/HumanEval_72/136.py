```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses two boolean conditions joined by the logical `and` operation to determine if the object `q` will fly:
1. The length of the queue `q` is equal to 1 or `q` is symmetric (`q == q[::-1]`). This checks if the queue is balanced.
2. The sum of the elements in queue `q` is less than or equal to the maximum weight `w`. 

These conditions ensure that the queue is balanced and its weight is within the acceptable range. If both conditions are met, the function returns `True`; otherwise, it returns `False`. 

Here is an example usage of the function:
```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
``` 
This example will print:
```bash
False
False
True
True
```

This function will return `True` if a flight is possible, and `False` otherwise, based on the conditions mentioned above.