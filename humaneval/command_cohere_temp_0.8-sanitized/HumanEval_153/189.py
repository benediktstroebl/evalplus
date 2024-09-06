def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        strength = cap - sm
        strengths[ext] = strength

    strongest_ext = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest_ext}'