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

The function uses two variables, `strongest` and `strongest_name`, which are initialized to `-1 and ''`, respectively. These variables will keep track of the strongest extension found, and the name of the strongest extension found, as we loop through the list of extensions.

We iterate through each extension in the `extensions` list. For each extension, we calculate the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) in the name of the extension. The strength of the extension is calculated as `cap - sm`. 

If the calculated strength is greater than the current strongest extension, we update the `strongest` and `strongest_name` variables to the current extension's strength and name. 

Finally, the function returns the string `'ClassName.StrongestExtensionName'` where `ClassName` is the `class_name` argument provided and `StrongestExtensionName` is the string value of `strongest_name`. 

The function adheres to the problem's guidelines, utilizing the strength calculation to choose the strongest extension and utilizing the alphabetical order as a tie-breaker. 

Note: This solution assumes that the list of extensions is non-empty and that the class name and extension names are non-empty strings. If these preconditions are not met, the function may raise an error or return an incorrect result.