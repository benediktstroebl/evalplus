```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap_count = sum(char.isupper() for char in extension)
        sm_count = sum(char.islower() for char in extension)
        strength = cap_count - sm_count
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'
```

The script uses a simple algorithm to find the strongest extension. First, it initializes the `strongest` variable to the smallest possible value (`-1` in this case). Then it loops through the extensions and calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the newly calculated strength is greater than the current strongest strength, the `strongest` and `strongest_index` variables are updated. Finally, the function returns the formatted string with the class name and the strongest extension name.