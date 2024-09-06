def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ""
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, ext
    return f'{class_name}.{strongest_name}'