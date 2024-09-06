```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The script uses a simple algorithmic approach to find the strongest extension. Initialize the strongest strength found so far to `-1` and the corresponding extension name to an empty string. Then loop through each extension in the list, calculating its strength as the difference between the number of uppercase and lowercase letters, and if the strength is greater than the current strongest, update the strongest strength and extension name. Finally, return the class name combined with the strongest extension name.