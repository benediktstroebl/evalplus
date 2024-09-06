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

The function uses a set data structure to solve the problem in an efficient manner. It iterates over the string, adding the current letter to the set. If the size of the set reaches or exceeds 3, we check if the current letter is already in the set. If so, the string is not happy, and we return False. If not, we continue with the iteration. The loop also checks if the length of the string is at least 3. If it isn't, we directly return False. Otherwise, if the loop completes without encountering any repeated letters in groups of 3 or more, we return True.

The problem is defined in a markdown code block with the following context:
```python
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
```

The expected output is a boolean value, True or False, depending on whether the given string is considered happy or not based on the provided criteria.