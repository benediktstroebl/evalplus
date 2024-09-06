def Strongest_Extension(class_name, extensions):
    strongest, strongest_index = -1, -1
 
    # Calculate the strength of each extension
    for ext_index, ext in enumerate(extensions):
        cap_count = ext.count('A') - ext.count('a')
        if cap_count > strongest:
            strongest, strongest_index = cap_count, ext_index
 
    # Return the strongest extension name
    return f'{class_name}.{extensions[strongest_index]}'
class_name = "MyClass"
extensions = ['AA', 'Bb', 'Cc', 'Aa', 'DD']