def Strongest_Extension(class_name, extensions):
    strongest, found = 0, -1
    for i, ext in enumerate(extensions):
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        strength = cap - sm
        if strength > strongest or (strength == strongest and i < found):
            strongest, found = strength, i
    return f'{class_name}.{extensions[found]}'