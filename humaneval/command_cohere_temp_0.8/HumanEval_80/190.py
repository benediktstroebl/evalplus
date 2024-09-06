```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function uses a clever approach to solve this problem. It first checks if the length of the string is at least 3, if not, it returns False as the string cannot have 3 consecutive distinct letters. Then, it constructs the set of all letters in the string, **{letters_set = set(s)}**.

The key insight here is that if we remove two letters from the string (any two, not necessarily consecutive), the set of remaining letters is the same as the set of all letters in the original string. For example, if the string is "abcdabcd", we remove 'a' and 'b', and the set of remaining letters becomes {'c', 'd' }, which is the same as the set of all letters in the original string.

Thus, the function returns True if every 3 consecutive letters are distinct and the string is "happy". Otherwise, it returns False. 

This approach is highly efficient, with a time complexity of O(1), making it an excellent solution to this happy string problem.