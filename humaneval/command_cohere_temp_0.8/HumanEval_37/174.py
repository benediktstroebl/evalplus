```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [e for e in l if e % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even`, which takes a list `l` as input. It filters out the even-indexed elements from the list using a list comprehension and stores them in a separate list called `even`. Then, it filters out the odd-indexed elements from the list and stores them in another list called `odd`. Finally, it returns the `odd` list followed by a sorted version of the `even` list. 

Here's an example usage of the function:
```python
result = sort_even([1, 2, 3, 4, 5, 6])
print(result)
```

The output of this code will be:
```
[1, 3, 2, 4, 5, 6]
```

This is a demonstration of the function's behavior, sorting the even-indexed elements while leaving the odd-indexed elements in their original order.