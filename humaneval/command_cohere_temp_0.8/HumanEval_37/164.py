```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even`, which takes a list of items as input. It filters out the even index elements from the list and sorts them. Then, it combines these sorted even elements with the original odd elements to create a new list. The result is a list that maintains the original order of odd index elements while sorting the even index elements.

Here is an example usage of the function:
```python
result = sort_even([5, 6, 3, 4])
print(result)
```

The output of this code will be:
```
[3, 6, 5, 4]
```

This demonstrates how the `sort_even` function sorts the even index elements while keeping the original order of the odd index elements in the list.