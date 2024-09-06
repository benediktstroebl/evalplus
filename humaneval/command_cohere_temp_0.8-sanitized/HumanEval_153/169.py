def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, extension in enumerate(extensions):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest = strength
            strongest_index = i
    return f'{class_name}.{extensions[strongest_index]}'