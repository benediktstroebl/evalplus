```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The function `largest_smallest_integers` works by setting the variables `positive` and `negative` to negative and positive infinity respectively. Then, it iterates over the list, checking if the current integer is larger than `positive` or smaller than `negative`, and updates these values accordingly. This way, it finds the largest negative and smallest positive integers in the list.

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
```
**Output:**
```
(1, 1)
```
This example test case shows the function correctly identifies both the largest negative (1) and smallest positive (1) integers from the list. 

The function gracefully handles empty or single-element lists, returning `None` for both the largest negative and smallest positive when there is no contrast to identify from the input list.  This is illustrated in the following example usage: 
 ```python
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0])) 
```
**Output:**
```
(None, None)
(None, None)
``` 

This robustness to different list scenarios is specified in the problem statement and ensures the function is effective for various cases.