def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        curr_strength = cap - sm
        if curr_strength > strength:
            strength = curr_strength
            strongest = ext
    return f'{class_name}.{strongest}'