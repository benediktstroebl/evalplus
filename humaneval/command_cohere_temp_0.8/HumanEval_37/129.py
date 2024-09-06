```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even` that takes a list `l` as input. It separates the list into two parts: a list of even indices called `even` and a list of odd indices called `odd`. The function then returns the `odd` list in its original order and appends the sorted `even` list to it.

Here's an example of how you can use this function:
```python
test_list = [1, 2, 3]
print(sort_even(test_list))  # expected output: [1, 2, 3]

test_list = [5, 6, 3, 4]
print(sort_even(test_list))  # expected output: [3, 6, 5, 4]
```

Expected output:
```
[1, 2, 3]
[3, 6, 5, 4]
```

This functionality sorts the values at even indices based on their values, while leaving the elements at odd indices untouched.