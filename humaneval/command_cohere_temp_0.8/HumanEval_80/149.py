```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] == s[i+1] and s[i] == s[i+2]:
            return False
        letters_set.add(s[i])
    return True
```

The function uses a set data structure to solve the problem, which is a good choice for checking if three consecutive letters are distinct. The key idea is to add each letter to a set and then check if the set size is less than 3 or not. If the size is less than 3, it means the set does not have three consecutive letters, so the string is happy.

The function returns False immediately if the string length is less than 3 to save computational time. Otherwise, it iterates over the string, adding each letter to the `letters_set` and checking if the set contains three elements and all are the same, which indicates three consecutive identical letters. If the criteria are met once, the function returns False. If no repeated pattern is found, it returns True at the end. 

This solution has a time complexity of O(n), where n is the length of the string, as it iterates over each letter in the string only once, and performs basic set operations with constant time complexity. 

Note: this solution assumes that the input contains only lowercase letters. If the input may contain non-alphabetic characters or is case-sensitive, additional checks and considerations may be necessary.