def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        s = cap - sm
        if s > strength:
            strength, strongest = s, ext
    return f'{class_name}.{strongest}'