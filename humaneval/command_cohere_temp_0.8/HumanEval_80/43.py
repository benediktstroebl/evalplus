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

The function uses a set data structure to solve the problem, which is optimized and preferable for this task. It iterates through the string, adding each letter to the `letters_set` set. Then, for each consecutive trio of letters, it checks if the set has a size of 3 and if so, whether the trio of letters are the same. The function returns False if any of these conditions are met and returns True if the string is happy. 

The above approach has a time complexity of O(n) where n is the length of the input string, and a space complexity of O(min(n, 3)) as it uses a set to store the letters, optimizing the space to be at most 3 letters. 

The tests cases would look like these:
```python
# Test cases
assert is_happy("abcd") == True
assert is_happy("adb") == True
assert is_happy("aabb") == False
assert is_happy("xyy") == False
assert is_happy("aaa") == False
assert is_happy("aaaa") == False
```