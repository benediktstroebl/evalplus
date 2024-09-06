```python
def same_chars(s0, s1):
    return sorted(s0) == sorted(s1)
```

The function `same_chars(s0, s1)` checks if two strings have the same characters independent of their position by sorting them first and then comparing. It works as follows:
1. Sort the characters in the two strings s0 and s1 using the sorted() function.
2. Compare the sorted strings using the equality operator (==).
3. Return the result of the comparison (either True or False) to indicate if the strings have the same characters. 

This approach takes into account the fact that characters in the strings may be in different orders, but the actual characters themselves are what matter for this problem.