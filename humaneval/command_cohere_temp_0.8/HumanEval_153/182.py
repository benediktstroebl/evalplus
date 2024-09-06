```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The script employs a simple loop to cycle through each extension, calculating the difference in counts between uppercase and lowercase letters to gauge the strength of each extension. The strongest extension is retained in the strongest variable, with its strength retained in the strength variable. In cases where multiple extensions share the same strength, the first-seen rule is applied, as per the problem's instructions. The function then returns the class name combined with the strongest extension, resulting in a string of the format ClassName.StrongestExtensionName.