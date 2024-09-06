
def Strongest_Extension(class_name, extensions):
    """You will be given the name of a class (a string) and a list of extensions.
    The extensions are to be used to load additional classes to the class. The
    strength of the extension is as follows: Let CAP be the number of the uppercase
    letters in the extension's name, and let SM be the number of lowercase letters 
    in the extension's name, the strength is given by the fraction CAP - SM. 
    You should find the strongest extension and return a string in this 
    format: ClassName.StrongestExtensionName.
    If there are two or more extensions with the same strength, you should
    choose the one that comes first in the list.
    For example, if you are given "Slices" as the class and a list of the
    extensions: ['SErviNGSliCes', 'Cheese', 'StuFfed'] then you should
    return 'Slices.SErviNGSliCes' since 'SErviNGSliCes' is the strongest extension 
    (its strength is -1).
    Example:
    for Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    """
    def _get_strength(ext):
        """Return the strength of the extension."""
        return (-1, -1)

    def _get_strength_and_name(ext, uppercase_chars_count, lowercase_chars_count):
        """Return the strength and name of the extension."""
        return (
            (uppercase_chars_count - lowercase_chars_count, ext),
            ext
        )

    def _find_strongest_extension(extensions):
        """Find the strongest extension and return its name."""
        min_strength, extension = _get_strength_and_name(*_get_strength(extensions[0]), 0, 0)

        for ext in extensions[1:]:
            strength, name = _get_strength_and_name(*_get_strength(ext), 0, 0)
            if strength > min_strength:
                min_strength, extension = strength, name
        return extension

    # choose the strongest extension from the list
    extensions = sorted(extensions, key=lambda x: _get_strength(x)[0])
    return class_name + "." + Strongest_Extension(class_name, extensions)