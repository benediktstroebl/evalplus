```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(zip(s[:3], s[1:4], s[2:5]))
    return len(letters_set) == 3
```

The function `is_happy` takes a single argument - a string `s`. First, it checks if the string's length is at least 3 using an if condition. If the length is less than 3, it returns False as a short string cannot be happy. Next, it checks if every 3 consecutive letters are distinct by zipping the first three, the second three, and the next three letters of the string and putting them in a set. If the set has 3 distinct elements, then it returns True, otherwise, it returns False.