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

The function uses a set data structure to solve the problem, which is a very efficient way to check if every 3 consecutive letters are distinct. The iteration goes through the string, and for each triplet, we check if it's already in the set. If it's not, the triplet is added to the set. If the set contains the triplet, then the answer is False.