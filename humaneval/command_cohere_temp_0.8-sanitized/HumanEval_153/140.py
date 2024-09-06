def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'