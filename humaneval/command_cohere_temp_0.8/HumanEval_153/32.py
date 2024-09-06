```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, ext
    return f'{class_name}.{strongest}'
```

The script follows a straightforward approach. The strength of each extension is calculated using the provided algorithm, and the strongest extension is initialized with the first extension in the list. Subsequently, the strength of each extension is compared to the strength of the current strongest extension, and if a stronger extension is found, the strongest extension and its strength are updated.

The script's performance is adequately efficient, given that its time complexity is proportional to the number of extensions, which is typically a relatively small quantity.

Should you require assistance with any more coding problems or anything else related to Python, don't hesitate to ask!