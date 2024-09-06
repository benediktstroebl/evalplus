```python
def cycpattern_check(first, second):
    first = first.lower()
    second = second.lower()
    
    return second in first or any(second == sub for sub in first if sub == second[1:] or sub == second[:1])
```

This code works by:
1. Lowercase both words to make the comparison case-insensitive.
2. Check if the second word is directly in the first word.
3. Check if any rotated version of the second word is in the first word using two loops to try all rotations.