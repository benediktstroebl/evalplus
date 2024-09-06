def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        if strength < cap - sm:
            strength = cap - sm
            strongest = e
    return f'{class_name}.{strongest}'