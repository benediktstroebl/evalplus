def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    strength = -(-len(strongest) - sum(c.isupper() for c in strongest))
    for ext in extensions[1:]:
        new_strength = -(-len(ext) - sum(c.isupper() for c in ext))
        if new_strength > strength:
            strongest = ext
            strength = new_strength
    return f'{class_name}.{strongest}'