def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap = sum(1 for char in extension if char.isupper())
        sm = sum(1 for char in extension if char.islower())
        strength = cap - sm
        if strength > strongest:
            strongest, strongest_index = strength, index
    return f'{class_name}.{extensions[strongest_index]}'