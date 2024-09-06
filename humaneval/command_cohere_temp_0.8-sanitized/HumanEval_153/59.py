def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for index, extension in enumerate(extensions):
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        # Assign strongest extension and its index
        if strength > strongest:
            strongest, strongest_index = strength, index

    return f'{class_name}.{extensions[strongest_index]}'