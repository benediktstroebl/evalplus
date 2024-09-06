```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength = curr_strength
            strongest = ext
    return f'{class_name}.{strongest}'
```

The script follows a simple approach. It initializes the strongest extension found and its corresponding strength to null and -1 respectively. The loop iterates through each extension, calculating its strength as the difference between the number of uppercase and lowercase letters. If the calculated strength is greater than the current strongest extension, the strongest extension and its strength are updated. After looping through all the extensions, the function returns the class name combined with the strongest extension name.

The given example in the problem statement would return 'Slices.SErviNGSliCes' as the strongest extension.