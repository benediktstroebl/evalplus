

def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return l[l.index(2)+1::l.index(2)+3::l.index(2)+4::l.index(2)+5::l.index(2)+6::l.index(2)+7::l.index(2)+8::l.index(2)+9::l.index(2)+10::l.index(2)+11::l.index(2)+12::l.index(2)+13::l.index(2)+14::l.index(2)+15::l.index(2)+16::l.index(2)+17::l.index(2)+18::l.index(2)+19
