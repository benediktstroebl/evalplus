```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The algorithm consists of two main parts:
1. Checking the length of the string. If it's less than 3 the string is not happy.
2. We create a counter for each letter to save the occurrence of each letter in the string. Then we iterate over the string in increments of 3 and check if the counter of each letter didn't exceed 1. If any of the counters exceed 1, the function returns False. Otherwise, it returns True. 

This solution runs in O(n) time complexity and O(1) space complexity, where n is the length of the input string s.