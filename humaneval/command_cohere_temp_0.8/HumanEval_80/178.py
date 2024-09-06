```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i + 1])] > 1 or letters_count[ord(s[i + 2])] > 1:
            return False
    return True
```

The problem is solved using an array of 128 elements to count the occurrences of the ASCII value of each letter in the string. The minimum length of a happy string is 3, so we iterate through the array in steps of 3 and check if the count of each letter in that step is more than 1; if so, return False. Otherwise, return True.

This approach guarantees a time complexity of O(n), where n is the length of the string, as we make a single pass to count the letters and make another pass to check for happiness, making it a feasible solution for small inputs.