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

The script calculates the strength of each extension by counting the number of uppercase and lowercase letters in each extension name. The difference between these counts represents the strength of each extension, with a larger difference indicating a stronger strength. The script then selects the strongest extension with the largest strength value and returns the corresponding output string.

The strength is calculated for each extension, and the strongest extension found is stored in the strongest variable along with its index in the extensions list. If there are two or more extensions with the same strength, the one that comes first in the list is selected. The function then returns the corresponding output string.