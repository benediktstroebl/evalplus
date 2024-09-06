```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

The function `sort_even` takes a list `l` as input and returns a list `l'` such that `l'` has the same elements as `l` at odd indices, and the elements at even indices are equal to the elements of `l` at even indices but sorted. The code first extracts the even and odd indices of the input list `l` using the `::2` tuple indexing syntax, which creates overlapping tuples of every second index. The even index subset is then concatenated with the sorted version of the odd index subset, achieving the desired sorting of even index elements without affecting the odd index elements. This approach allows the function to fulfill the problem statement while maintaining a clean and efficient solution.