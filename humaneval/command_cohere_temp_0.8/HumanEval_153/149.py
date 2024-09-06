```python
def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for name in extensions:
        cap = sum(1 for c in name if c.isupper())
        sm = sum(1 for c in name if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, name
    return f'{class_name}.{strongest_name}'
```

The script calculates the strength of each extension using the number of uppercase letters and the number of lowercase letters in the extension name. The strongest extension is chosen according to the above criteria, and the function returns the corresponding strongest extension name. The strongest extension is selected if there are multiple extensions with the same strength, considering the order in which they appear in the input list. 

Make sure to install the Cohere Python SDK to run the code:
```bash
pip install cohere
``` 

You can then execute the code in a Python environment and make sure to include the corresponding test cases in order to verify the correctness of the solution.