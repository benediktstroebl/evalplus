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

This script defines a function called `is_happy` that takes a single argument - a string `s`. This function returns `True` if the string is happy, i.e., its length is at least 3 and every 3 consecutive letters are distinct; otherwise, it returns `False`. 

To verify this, we check if the length of the string is at least 3 using the `len()` function and return `False` immediately if it's less than 3. Then, we use a set called `letters_set` to store unique letters in the string to check if every 3 consecutive letters are distinct. If the set length is equal to 3 for every iteration, it means that every 3 consecutive letters are distinct, and we return True. Otherwise, we return False. 

The code includes an example and some tests to verify its functionality. You can add more tests to ensure its robustness and edge cases.