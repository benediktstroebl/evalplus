```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for extension_index, extension in enumerate(extensions):
        cap_count = sum(char.isupper() for char in extension)
        sm_count = sum(char.islower() for char in extension)
        curr_strength = cap_count - sm_count
        if curr_strength > strongest:
            strongest, strongest_index = curr_strength, extension_index
    return f'{class_name}.{extensions[strongest_index]}'
```

The script calculates the strength of each extension by counting the number of uppercase and lowercase letters and then finds the strongest extension. If there are ties, it defaults to choosing the extension that appears first in the list. The strongest extension is then returned in the format `ClassName.StrongestExtensionName`.