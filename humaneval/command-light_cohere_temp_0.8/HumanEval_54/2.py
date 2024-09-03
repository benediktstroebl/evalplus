```python
def same_chars(s0: str, s1: str):
    return len(set(s0)) == len(set(s1))

# Testing the function...
print(same_chars('eabcd', 'dddddddabce'))  # Output: True
print(same_chars('eabcd', 'ddedab'))    # Output: False
print(same_chars('aa', 'a'))        # Output: True
print(same_chars('bb', 'ab'))        # Output: False
```
This code has a function `same_chars` that checks if two given strings have the same characters. The function uses the basic idea of counting the unique characters in both strings and returns `True` if the lengths are equal. 

Note that: You can think of this problem as finding pairs of characters that are present in both strings but not present in either.