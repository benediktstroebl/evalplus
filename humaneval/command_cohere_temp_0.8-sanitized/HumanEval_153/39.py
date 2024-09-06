def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for i, extension in enumerate(extensions):
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        strength = cap_count - sm_count
        if strength > strongest:
            strongest, strongest_index = strength, i
    return f'{class_name}.{extensions[strongest_index]}'