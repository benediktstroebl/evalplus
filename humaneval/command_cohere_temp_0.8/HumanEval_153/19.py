```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, extension in enumerate(extensions):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'
```

The function calculates the strength of each extension as the difference between the number of uppercase and lowercase letters in the name. The strongest extension is selected, and if there are ties, it prefers the one that appears first in the list. The function returns the class name combined with the strongest extension. This approach ensures efficiency in both time and space complexity, making it suitable for real-world applications.