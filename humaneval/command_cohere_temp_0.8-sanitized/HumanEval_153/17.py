def Strongest_Extension(class_name, extensions):
    strengths = {}
    for e in extensions:
        cap = sum(1 for c in e if c.isupper())
        sm = sum(1 for c in e if c.islower())
        cur_strength = cap - sm
        strengths[e] = cur_strength
    
    strongest = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest}'