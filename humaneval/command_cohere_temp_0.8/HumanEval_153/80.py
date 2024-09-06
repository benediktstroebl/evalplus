```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = 0, 0
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function uses two nested loops to iterate through the list of extensions and calculate the strength of each extension based on the number of uppercase and lowercase letters. The strength is calculated as the difference between the number of uppercase letters and the number of lowercase letters. The function then finds the strongest extension by comparing the strength of each extension and keeps track of the index of the strongest extension. Finally, the function returns the extension of the class with the strongest extension.