```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

This Python script defines a function called `is_happy` that takes a single string parameter `s`. The function returns `True` if the string is happy, and `False` otherwise. The purpose of this function is to determine if a given string satisfies the condition required to be considered happy.

The condition for a string to be considered happy is defined by the following rules:
1. The string's length must be at least 3 characters.
2. For every consecutive group of 3 letters in the string, each letter must be distinct from the other two.

The function uses a set called `letters_set` to store the encountered letters in the string. It iterates over the characters of the string in increments of 2. Then, it checks if each group of 3 consecutive letters forms a unique set. If so, the string is considered happy, and the function returns `True`. If the condition is not met, it returns `False`.

This implementation ensures that the function is self-contained and provides the expected results for the given problem. It is concise and straightforward to understand. The total time complexity of this code is O(n), where n is the length of the string `s`, as it iterates over each consecutive trio of letters only once. The average complexity per iteration is O(1), as it only requires checking sets of three letters. Thus, the total complexity remains linear.