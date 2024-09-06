```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 256
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The code first checks if the string's length is at least 3, then it counts the occurrences of each letter in the string using a 256-element array. If any of the consecutive letters at intervals of 3 are repeated, the function returns False, otherwise, it returns True. The code should ideally have a timestep complexity of O(1), and use O(n) space where n is the length of the given string. 

This solution can efficiently handle any input within seconds as the worst-case time complexity is O(1). Also, the space complexity is O(1) and unaffected by the input size. 

Note: this solution assumes only uppercase letters, but any further development should also account for lowercase and other characters too.