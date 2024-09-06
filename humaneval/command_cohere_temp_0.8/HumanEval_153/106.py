```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength, strongest = curr_strength, ext
    return f'{class_name}.{strongest}'
```

The script follows a straightforward approach. The `Strongest_Extension` function takes in the class name and a list of extensions as inputs. It initially sets the `strongest` extension and its strength to indices `-1` (`-1, -1`) to represent the initial values.

Then, it iterates through each extension in the input list. For each extension, it calculates the number of uppercase letters (`cap`) and the number of lowercase letters (`sm`) in the extension name. It computes the strength as the difference between these counts.

If the calculated strength is greater than the current strongest extension, the script updates the strongest extension and its corresponding strength. This process ensures that the strongest extension is selected based on the updated strength.

Finally, the function returns the formatted result in the desired format, `'ClassName.StrongestExtensionName'`, using the `f-string` approach.