```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, e
    return f'{class_name}.{strongest_name}'
```

The script uses a simple loop to iterate through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters. If the strength is greater than the current strongest extension, the variables are updated. Lastly, the function returns the formatted string with the class name and the strongest extension.