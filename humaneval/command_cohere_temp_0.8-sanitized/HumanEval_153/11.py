def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for ext_index, ext in enumerate(extensions):
        cap = sum(char.isupper() for char in ext)
        sm = sum(char.islower() for char in ext)
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, ext_index
    return f'{class_name}.{extensions[strongest_index]}'