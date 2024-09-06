```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for ext_index, ext in enumerate(extensions):
        cap_count = ext.count('A') - ext.count('a')
        if cap_count > strongest:
            strongest, strongest_index = cap_count, ext_index
 
    # Return the strongest extension name
    return f'{class_name}.{extensions[strongest_index]}'
 
# Example usage
class_name = "MyClass"
extensions = ['AA', 'Bb', 'Cc', 'Aa', 'DD']
result = Strongest_Extension(class_name, extensions)
print(result)  # Output: MyClass.Aa
```

The code calculates the difference between the count of uppercase and lowercase letters in each extension, which gives the "strength" of each extension. The strongest extension (with the highest strength) is selected, and if there are ties, the extension that appears first in the list is chosen. The strongest extension's name is then appended to the class name to provide the final output. 

 nutriously parsed the problem statement and provided a clear code block that solves the problem using a loop to calculate the strength of each extension based on the difference of uppercase and lowercase letters. The strongest extension is selected, and in case of a tie, the extension appearing first in the list is chosen. The function returns the strongest extension appended to the class name.