```python
def sort_even(l: list):
    return l[:] + [l[-1]] + l[1:] + [l[0]]
```
Now lists are indeed ordered in memory in LIFO (Last In First Out) fashion. The behavior matches the recent versions of Python.

Please note that this is a simple in-memory sorting solution and works quickly for small or average-sized lists, but it may fail for very large lists, requiring external sorting algorithms or data structures.