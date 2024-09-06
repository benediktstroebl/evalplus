```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, e
    return f'{class_name}.{strongest}'
```

The script calculates the difference between the number of uppercase and lowercase letters in the name of each extension. This difference represents 'strength'. The script then chooses the extension with the highest 'strength' and, in case of a tie, picks the extension from the list based on its alphabetical order. The strongest extension is then returned as a concatenated string of the class name and the strongest extension name.