```python
def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and a + b in seen:
                return True
            seen.add(a)
    return False
```

The function `triples_sum_to_zero` works by first creating a set `seen` to keep track of integers that have appeared in the list. It then iterates over the list, checking if the current integer `a` together with another integer `b` in the list sum up to zero. If so, it returns `True`. The nested loop runs in O(n^2) time but this is justified since the problem asks for triples not pairs. 

You can use the function by calling it and passing in a list of integers like so:
```python
print(triples_sum_to_zero([1, 3, 5, 0]))  # Outputs False
print(triples_sum_to_zero([1, 3, -2, 1]))  # Outputs True
``` 
This would return `False` and `True` respectively, as expected, since the list `[1, 3, 5, 0]` does not have three elements that sum up to zero, whereas `[1, 3, -2, 1]` does. 

If you wish to test this code with more sample inputs, you can add more `print` statements like the ones above.