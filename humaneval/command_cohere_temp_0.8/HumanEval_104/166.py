```python
def unique_digits(x):
    odd = [int(''.join(c for c in str(i) if c % 2 != 0)) for i in x if int(''.join(c for c in str(i) if c % 2 != 0)) <= max(x)]
    return sorted(odd)
```

The algorithm for this solution is:
1. Convert each integer in the input list to a string.
2. Use a list comprehension to filter out odd digits using the condition `c % 2 != 0`.
3. Convert the filtered string back to an integer.
4. Store these filtered integers in the `odd` list.
5. Return a sorted version of the `odd` list. 

This solution takes advantage of Python's string manipulation capabilities and list comprehension to effectively filter out the desired integers.