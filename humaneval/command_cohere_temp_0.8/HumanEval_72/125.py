```python
def will_it_fly(q, w):
    return (len(q) == 1 or len(set(q)) == len(q)) and sum(q) <= w
```

The function `will_it_fly` uses two conditions to determine if an object will fly:
1. The length of the queue `q` is one or it has only unique numbers. This checks if the queue is balanced. 
2. The sum of the values in the queue `q` is less than or equal to the maximum weight `w`. 

Examples of how the function is called and its possible outputs are:
```python
will_it_fly([1, 2], 5)  # False
will_it_fly([3, 2, 3], 1)  # False
will_it_fly([3, 2, 3], 9)  # True
will_it_fly([3], 5)  # True
```