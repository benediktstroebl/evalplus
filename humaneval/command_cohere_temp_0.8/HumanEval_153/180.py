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

The function uses two variables, `strongest` and `found`, to keep track of the strongest extension found so far and the index of the strongest extension in the list. The loop iterates through each extension in the list, calculating the strength of the extension as the difference between the number of uppercase and lowercase letters in the extension name. If the current extension has a greater strength than the current strongest extension, or has the same strength but appears earlier in the list, the `strongest` and `found` variables are updated.

After iterating through all the extensions, the function returns the formatted string with the class name and the strongest extension name. If there are multiple extensions with the same strength, the one that appeared first in the list is selected. 

This approach assumes that the extension names are purely alphabetical characters, and does not consider any characters other than uppercase and lowercase letters in determining the strength. It efficiently finds the strongest extension by keeping track of the strongest found so far and the index of the strongest extension, updating them whenever a stronger extension is found.