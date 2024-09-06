```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        strengths[ext] = strength
    strongest_ext = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest_ext}'
```

The function uses a dictionary called `strengths` to keep track of the strength of each extension, where the strength is calculated as the difference between the number of uppercase and lowercase letters in each extension name. After calculating the strength of each extension, it finds the strongest extension key in the `strengths` dictionary using the `max` function with the `key` parameter set to `strengths.get`. 

The function subsequently returns the strongest extension name concatenated with the class name using a format string. This approach ensures that the strongest extension is selected based on its strength value, with ties broken in favor of extensions that appear first in the input list.