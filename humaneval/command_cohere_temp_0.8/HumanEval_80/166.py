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

The function uses a set data structure to solve the problem. The algorithm traverses the string and adds letters into a set. If the set size is less than 3, the algorithm continues iterating. If the set size is at least 3, the algorithm checks if the current letter is the same as the previous 2 consecutive letters. If so, the function returns False. If the condition is fulfilled for every 3 consecutive letters, the function returns True. 
The solution is efficient and has a time complexity of O(n), where n is the length of the input string s. It also has a space complexity of O(min{n, 3}) as it only holds 3 letters at a time in the set.