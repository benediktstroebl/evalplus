import unittest
def Strongest_Extension(class_name, extensions):
    strongest, strength = None, 0
    for ext in extensions:
        cap = sum(c.isupper() for c in ext)
        sm = sum(c.islower() for c in ext)
        delta = cap - sm
        if delta > strength or (delta == strength and ext < strongest):
            strength = delta
            strongest = ext
    return f'{class_name}.{strongest}'