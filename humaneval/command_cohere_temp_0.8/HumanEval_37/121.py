```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function `sort_even` that solves the problem as described in the prompt. It first identifies the even and odd indexed elements of the input list, using list comprehensions. The even-indexed elements are extracted into a separate list, which is then sorted. The function returns the original odd-indexed elements, followed by the sorted even-indexed elements, resulting in the desired sorted output.