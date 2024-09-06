```python
def Strongest_Extension(class_name, extensions):
    strengths = {}
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        cur_strength = cap - sm
        strengths[e] = cur_strength
    
    strongest = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest}'
```

The script uses a dictionary `strengths` to keep track of the strength of each extension, calculated as the difference between the number of uppercase and lowercase letters. After calculating the strength of each extension, the script finds the strongest extension using the `max` function with the `key` parameter set to the dictionary value (`strengths.get`).

The `strengths` dictionary is sent to the `key` parameter to search for the maximum value key, and the value associated with that key is set as the strongest extension.

The code tests on the following example:
```python
>>> Strongest_Extension('my_class', ['AA', 'Be', 'CC'])
'my_class.AA'
```

The script returns the expected output `'my_class.AA'` as 'AA' has all uppercase letters, meaning its strength is `0`, which is the strongest strength possible.