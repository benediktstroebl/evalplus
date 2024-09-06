def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        ext_strength = cap - sm
        if ext_strength > strength:
            strength, strongest = ext_strength, e
    return f'{class_name}.{strongest}'