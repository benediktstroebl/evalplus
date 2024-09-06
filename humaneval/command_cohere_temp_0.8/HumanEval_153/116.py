```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The function uses two variables, `strongest` and `found`, to keep track of the current strongest extension and the index of this extension in the `extensions` list. The variable `found` is initially set to -1 to indicate that a strongest extension has not yet been found.

The function then iterates through each extension in the `extensions` list using a loop. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) in the extension name. It then calculates the `strength` of the extension as the difference between `cap` and `sm`.

If the `strength` of the current extension is greater than the current strongest strength, the variables `strongest` and `found` are updated to store the new strength and the index of the strongest extension so far.

After iterating through all the extensions, the function returns the formatted string containing the class name and the name of the strongest extension, using the index stored in `found` to access the strongest extension in the list.

This algorithm has a time complexity of `O(n)` where `n` is the length of the `extensions` list, since it iterates through each element once, performing constant time operations for each element.