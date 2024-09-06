```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'
```

The function analyzes each extension to determine its strength, quantifies the number of uppercase and lowercase letters, and computes the difference to determine the strength score. The function then identifies the strongest extension by comparing the strength values and, once identified, the index of the strongest extension in the list. Ultimately, the function returns the class name combined with the strongest extension. 

This problem can also be solved using recursion.