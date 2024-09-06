def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        curr_strength = cap - sm
        if curr_strength > strength:
            strength = curr_strength
            strongest = ext
    return f'{class_name}.{strongest}'