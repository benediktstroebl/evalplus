```python
def will_it_fly(q, w):
    return (len(q) == 1 or q == q[::-1]) and sum(q) <= w
```

The function `will_it_fly` uses two conditions to determine if an object will fly:
1. The length of the queue `q` is equal to 1 or `q` is equal to its reversed version. This checks if the queue is balanced (palindrome). 
 2. The sum of the elements in queue `q` is less than or equal to the maximum weight `w`. 

Return `True` if both conditions are met; otherwise, return `False`. 

Here is an example usage of the function:
```python
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
``` 
This should output:
```bash
False
False
True
True
```
This function will return `True` if the object will float and `False` otherwise.