def Strongest_Extension(class_name, extensions):
    strongest, strength = None, -1
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        if strength < 0 or (cap - sm > strength and strength != -1):
            strongest, strength = ext, cap - sm
    return f'{class_name}.{strongest}'