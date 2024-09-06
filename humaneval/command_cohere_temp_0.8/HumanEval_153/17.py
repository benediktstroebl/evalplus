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

The script uses a simple loop to iterate through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the strength is higher than the current strongest extension, the variables storing the strongest strength and its index are updated.

At the end of the loop, the function returns the formatted string with the class name and the strongest extension name. This approach is efficient and easy to understand, following the linear flow of loops to solve the problem. It also adheres to the guideline of choosing the strongest extension based on strength values and selecting the first extension in case of ties.