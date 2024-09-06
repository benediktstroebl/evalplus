```python
def sort_even(lst):
    even = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    lst = lst[:-]
    even.append(sum(even))
    return even
```