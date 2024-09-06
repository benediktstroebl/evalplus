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

The script employs a loop to examine each extension, assessing the uppercase and lowercase letters to determine the strength of each extension, then saves the highest strength and its corresponding index. Finally, it utilizes the strongest extension's index to construct and return the required string. This algorithm successfully solves the problem. 

The implementation has a time complexity of `O(n)` since it iterates over the list of extensions once, which makes it efficient enough to tackle the problem in a reasonable amount of time for reasonable inputs.