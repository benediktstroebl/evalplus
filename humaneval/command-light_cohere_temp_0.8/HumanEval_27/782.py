```python
def flip_case(string: str) -> str:
    new_string = ""
    for char in string:
        if char.isalpha():
            new_string += char.isupper()
        ' '
        else:
            new_string += char.islower()
    small letters in a case. for the same.  # the also for special case, this function flips the case of all characters in a given string.
```