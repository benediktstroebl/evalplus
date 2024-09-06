```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The function works by initializing the strongest strength found and the corresponding extension name to -1 and an empty string respectively. It then iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the strength is greater than the current strongest extension, the strongest strength and name are updated. Finally, the function returns the class name and the strongest extension name concatenated with a dot in between.

Here's an example of how you can use the function:
```python
class_name = "MyClass"
extensions = ["AA", "Be", "CC", "aa", "Bb", "Cc"]
result = Strongest_Extension(class_name, extensions)
print(result)  # Output: MyClass.AA
```

This will return "MyClass.AA" since the strongest extension is "AA" with a strength of 0, which occurs first in the list.