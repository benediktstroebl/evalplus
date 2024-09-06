def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if (cap - sm > strength) or (cap - sm == strength and ext < strongest):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'