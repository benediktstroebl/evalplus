```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

The logic here is to take characters in `s` that aren't in `c`, and reverse them to be at the start. Then add characters in `s` that are in `c` to the end. This means the characters in `c` are effectively removed from `s`, and the palindrome check is relatively simple. You compare the result to its reverse, which can be done in-place with Python's slicing. This solution is algorithmically efficient and elegantly simple.