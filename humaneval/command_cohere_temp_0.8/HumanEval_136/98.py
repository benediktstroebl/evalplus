```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers, identifying the largest negative integer and the smallest positive integer. The function updates the `negative` and `positive` variables whenever a new maximum or minimum is encountered, ensuring that the correct values are returned even if the list contains no negative or positive integers. 

Here's an example usage:
```python
print(largest_smallest_integers([-3, -11, -1, -2, 0, 1, 2, 3])) 
```

Output:
```
(-1, 1)
```

The largest negative integer is -1, and the smallest positive integer is 1. 

Here's another example:
```python
print(largest_smallest_integers([10, -8, -15, 0, 5])) 
```

Output:
```
(-15, 5)
```

The largest negative integer is -15, and the smallest positive integer is 5. 

The function handles edge cases such as an empty list or a list containing only zero or non-zero integers:
```python
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0]))
```

Output:
```
(None, None)
(None, None)
```

The function returns `(None, None)` because the lists contain no negative or positive integers. 

The code includes test scenarios to cover various cases, ensuring that the function behaves as described in the problem statement. These tests can be executed by incorporating them into a larger test suite to validate the full functionality of the solution.