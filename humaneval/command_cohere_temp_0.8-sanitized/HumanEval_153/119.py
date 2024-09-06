def Strongest_Extension(class_name, extensions):
    strengths = {}
    for ext in extensions:
        cap = sum(1 for c in ext if c.isupper())
        sm = sum(1 for c in ext if c.islower())
        if (cap, sm) in strengths:
            if strengths[(cap, sm)] >= len(ext):
                strongest = ext
        strengths[(cap, sm)] = len(ext)
    return f'{class_name}.{strongest}'