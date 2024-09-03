```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, e
    return f'{class_name}.{strongest}'
```

The function works by finding the extension with the highest negative strength, which is the closest to 0, in the list of extensions. The function initializes the `strongest` and `strength` variables to the lowest possible values (`-1`) to ensure that any valid input will result in the strongest extension being selected.

The function then iterates over each extension and calculates its strength by counting the number of uppercase and lowercase letters in the extension. If the strength is greater than the current strongest extension, the function updates the `strongest` and `strength` variables.

Finally, the function returns the string of the class name and the strongest extension name concatenated with a dot in between.

The strength is calculated as the difference between the number of uppercase and lowercase letters. This is a valid approach to solve this problem, since the extension with the most uppercase letters is considered the strongest.