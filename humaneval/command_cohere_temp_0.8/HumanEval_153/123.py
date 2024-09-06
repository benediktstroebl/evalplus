```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The script uses a for loop to iterate through each extension in the `extensions` list. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) using summation operations. It computes the strength of the extension as the difference between `cap` and `sm`, assigning it the current maximum strength if it's stronger than the previous strongest extension. Finally, the function returns the formatted result string.