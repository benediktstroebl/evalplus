```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        if strength < 0 or (cap - sm > strength):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'
```

The function uses two nested loops to iterate through each extension in `extensions`. It determines the strength of each extension as the difference between the number of uppercase letters and the number of lowercase letters in the extension name. This strength is saved in the `strength` variable. If the strength of the current extension is greater than the previously recorded strength, the variables storing the strongest extension and its strength are updated.

Finally, the function returns the string formatted with the class name and the strongest extension name. 

This solution assumes that the list of extensions passed to the function is not empty. If you would like to handle this edge case and ensure the function behaves correctly when passed an empty list, let me know and I will be happy to modify the code accordingly. Feel free to ask if you would like any further explanations.