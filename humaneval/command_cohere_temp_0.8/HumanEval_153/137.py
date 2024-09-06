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

The function uses two variables, `strongest` and `found`, to keep track of the strongest extension found so far and the index of the strongest extension in the list of extensions, respectively. The function then iterates through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase letters and the number of lowercase letters in the extension. If the strength of the current extension is greater than the strength of the current strongest extension, or if the strengths are equal but the current extension appears earlier in the list, the values of `strongest` and `found` are updated.

Once the loop has finished iterating through the list of extensions, the function returns the string `'ClassName.StrongestExtensionName'`, where `ClassName` is the input `class_name` and `StrongestExtensionName` is the name of the strongest extension, which is located at the index `found`. 

This solution assumes that the list of extensions is case-insensitive sortable, e.g., you can sort the list ['StuFfed', 'Cheese', 'SErviNGSliCes'] and the result will be ['Cheese', 'SErviNGSliCes', 'StuFfed'].  This is the case for many common languages like Python, but not for case-sensitive languages such as Java.