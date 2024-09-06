```python
def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'
```

The function loops through the list of extensions, calculating the strength of each extension as the difference between the number of uppercase and lowercase letters in the extension name. If the calculated strength is higher than the current strongest extension, the strongest extension and its strength are updated. After looping through all extensions, the function returns the class name combined with the strongest extension name. 

The strength metric is designed to give more weight to extensions with more uppercase letters, suggesting stronger or more significant extensions, whereas lowercase letters suggest peripheral or less crucial extensions. In the event of a tie in strength, the function will return the first extension in the list. 

This approach assumes that the extensions list is already sorted alphabetically. If the list is not sorted, the strongest extension may not be selected correctly in the case of a strength tie. Feel free to adjust the script to that end if that information is disclosed later on in the context of the problem. 

This algorithm runs in O(n) time, where n is the length of the `extensions` list, making it efficient for handling lists of varying sizes.