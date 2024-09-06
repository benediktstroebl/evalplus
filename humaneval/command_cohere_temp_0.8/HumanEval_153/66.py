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

The function analyzes each extension, calculating the difference between the count of uppercase and lowercase letters. This difference indicates the "strength" of the extension. The idea is that capitalized letters tend to provide more protection, making the class more robust and secure.

The script then returns the class name combined with the strongest extension, ensuring the class is optimally fortified.

Note that this is a straightforward solution, albeit not the most efficient one. It would be critical to consider more optimal approaches for larger lists of extensions to ensure scalability and performance.