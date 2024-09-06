```python
def sort_even(l):
    even, odd = zip(*[(i, v) for i, v in enumerate(l) if i % 2 == 0])
    return [o if i % 2 else e for i, (e, o) in enumerate(zip(odd, even))]
```

Here's a brief explanation of how it works:
- The function 'sort_even' takes a list 'l' as input.
- It splits the list into two parts using tuple unpacking 'even' and 'odd', even and odd indices respectively, by utilizing the 'enumerate' function and a condition on the index 'i' to determine whether it is even or odd.
- It then zips these two parts together, pairing up corresponding elements, and returns the resulting list 'l' where the even-indexed elements are sorted.