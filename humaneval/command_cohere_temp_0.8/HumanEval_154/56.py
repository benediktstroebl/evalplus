```python
def cycpattern_check(first, second):
    return second in set(map(lambda x: x[:len(second)] , (iter(first.upper()) if len(first) > len(second) else iter(first))))
``` 

The problem asks whether the second string or any of its rotations are sub-strings in the first string. The upper case version of the first string is created to ease the process of finding rotations as rotations of upper case strings have a fixed length and do not contain spaces, thus we can check if the second string is one of its rotations. The `map` and `iter` functions are used to generate all rotations and subsequently filter the necessary ones using `set`. The outcome is then returned as a boolean value.