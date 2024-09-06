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

The function `largest_smallest_integers` works by setting the initial values of `positive` and `negative` to negative and positive infinity respectively. It then iterates over the list, checking if each element is a larger positive number than previous ones, or a more negative number than previous ones, updating the values accordingly. Finally, the function returns a tuple containing the largest negative integer, and the smallest positive integer among the list, or `None` if there are none. 

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
```

The output of this code will be:
```
(None, 1)
```

This indicates that the largest negative integer is `None`, and the smallest positive integer is `1`. 

The function also handles edge cases, such as an empty list or a list containing only zero, correctly returning `(None, None)`.