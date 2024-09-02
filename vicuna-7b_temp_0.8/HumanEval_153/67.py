
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
    def chains(items):
        """Yields all possible chains of items, in order from start to end."""
        start = items[0]
        end = items[0]
        for item in items[1:]:
            end.append(item)
            start = end[-1]
        yield start
        yield end
        end.pop() # last element should not be present
        start.extend(end) # bring all but last element back to start
        for sublist in chains(items[1:]):
            yield ''.join(sublist)

    chain_items = chains([extensions.index(ext) for ext in extensions])
    chain_items = sorted(chain_items, key=lambda x: x[1], reverse=True)
    best_ext = chain_items[0][0]
    best_ext_name = class_name + "." + best_ext
    return best_ext_name