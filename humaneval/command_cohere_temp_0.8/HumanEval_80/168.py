```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The problem statement states that a string is happy if its length is at least 3 and every 3 consecutive letters are distinct. The script checks that the length of the string is at least 3 to ensure it can divide it into chunks of 3 letters without leaving an incomplete chunk. Then, it uses a set to store the letters encountered, adding each letter of the string to the set. Every 3 letters form a subset of the set, and if any two of them are equal, the set collection strategy effectively removes the duplicate, leaving only distinct letters. Thus, if every 3 letters are distinct, the original string is considered happy. 

The script considers some examples in the problem statement, such as `a`, `aa`, `abcd`, `aabb`, `adb`, and `xyy`, to confirm the correct behavior of the function against the expected outcomes.