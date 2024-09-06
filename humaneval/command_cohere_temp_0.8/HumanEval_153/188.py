```python
def Strongest_Extension(class_name, extensions):
    strongest, found = -1, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The script calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. The strongest extension is selected, considering both strength and sequence if there is a tie.

The code maintains a variable `found` to track the index of the strongest extension after finding the strongest strength. This ensures that if multiple extensions have the same strength, the one encountered first in the list will be selected. 

The ` strongest, found = -1, -1` line initializes the variables `strongest` and `found` to `-1` which allows the script to track the strongest extension found so far and its index in the `extensions` list. 

Overall, the provided code follows a systematic approach to solve the problem, which is both efficient and easy to understand.