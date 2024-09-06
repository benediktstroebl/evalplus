import unittest
def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el != '']
    lst.sort(key=lambda x: (-len(x), x))
    return lst