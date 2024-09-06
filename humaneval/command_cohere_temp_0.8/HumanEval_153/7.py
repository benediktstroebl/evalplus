```python
def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'
```

The script uses a loop to iterate through each extension in the list, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. If the strength of that extension is higher than the strongest strength found so far, or if it's equal in strength to the strongest extension but appears earlier in the list, the script updates the strongest extension and its index in the list. After looping through all extensions, the script returns the strongest extension in the format `ClassName.StrongestExtensionName`.