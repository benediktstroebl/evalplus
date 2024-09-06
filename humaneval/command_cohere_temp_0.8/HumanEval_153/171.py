```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f"{class_name}.{strongest_name}"
```

The function works by initializing the strongest strength found so far to -1, and the corresponding extension name to an empty string. It then iterates through each extension, calculating the strength of the extension by counting the number of uppercase and lowercase letters in the name. If the calculated strength is greater than the current strongest strength, the strongest strength and corresponding extension name are updated.

After processing all extensions, the function returns the strongest extension using the format `class_name.strongest_extension_name`. If there are multiple extensions with the same strength, the one that appears first in the list is selected.

The implementation is efficient because it uses Python's string methods (`''.isupper()'` and `''.islower()'`) to find the number of uppercase and lowercase letters. Therefore the time complexity is O(N), where N is the length of the list of extensions.

The space complexity is O(1) since the additional space used is limited to storing the two variables with the strongest strength and name. 

Note that the original problem statement mentions that the class name and list of extensions are given as command-line arguments. For the given self-contained Python script, we assume that the `class_name` and `extensions` are passed as function parameters. Adjustments may be needed if you are evaluating the script through an IDE or an actual command line.