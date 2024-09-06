```python
def reverse_delete(s, c):
    s = [x for x in s if x not in c]
    s = ''.join(s)
    return s, s == s[::-1]
```

The problem is solved in two main steps:
1. Remove all characters from `s` that are present in `c` using a list comprehension.
2. Restore the changed string to a single string and check if it's a palindrome by comparing it with its reverse using slicing. 

The code tests demonstrate its usage on various inputs to ensure it produces the correct palindrome determination. Feel free to adapt and extend the test code for your specific needs or to explore more complex scenarios.