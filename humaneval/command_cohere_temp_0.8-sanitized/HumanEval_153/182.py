def Strongest_Extension(class_name, extensions):
    strongest, strongest_name = -1, ''
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_name = strength, ext
    return f'{class_name}.{strongest_name}'