def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        delta = cap - sm
        if delta > strength or (delta == strength and ext < strongest):
            strength = delta
            strongest = ext
    return f'{class_name}.{strongest}'