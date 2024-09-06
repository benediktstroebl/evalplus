def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        cur_strength = cap - sm
        if cur_strength > strength:
            strength, strongest = cur_strength, ext
    return f'{class_name}.{strongest}'