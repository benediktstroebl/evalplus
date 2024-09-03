def Strongest_Extension(class_name, extensions):
    def calc_strength(name):
        return sum(1 for char in name if char.isupper()) - sum(1 for char in name if char.islower())

    strongest = max(extensions, key=calc_strength)
    return f"{class_name}.{strongest}"