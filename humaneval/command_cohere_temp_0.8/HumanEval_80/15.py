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

The function uses a set data structure to solve the problem. It first checks if the length of the string is at least 3, if not, it returns False. Then, it checks if the set contains 3 elements and those elements occur consecutively in the string, if so, it returns False. If none of these conditions are met, the function returns True. 

Here is an example of a happy string: 'abcd'. Each consecutive trio of letters is unique, as is the case for 'xyy' - threes are distinct. 

Unhappy examples include 'aabb', 'aa', and 'xyyx'.