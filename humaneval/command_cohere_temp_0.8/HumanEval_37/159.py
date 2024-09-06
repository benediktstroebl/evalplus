```python
def sort_even(l):
    even = [e for e in l if e % 2 == 0]
    odd = [e for e in l if e % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even` which takes a list of numbers as input. It separates the even and odd numbers using list comprehension and then returns the odd numbers followed by a sorted list of even numbers. The expected output is obtained by taking the original list and replacing the even numbers with the sorted version, while keeping the odd numbers in their original places.