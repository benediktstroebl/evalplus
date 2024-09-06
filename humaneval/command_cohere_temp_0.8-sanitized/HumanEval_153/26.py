def Strongest_Extension(class_name, extensions):
    strongest, strength = -1, -1
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if strength < 0 or (cap - sm > strength):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'