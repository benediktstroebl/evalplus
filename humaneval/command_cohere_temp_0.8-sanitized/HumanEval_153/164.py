def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    strongest_strength = 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest_strength:
            strongest = ext
            strongest_strength = strength
    return f'{class_name}.{strongest}'