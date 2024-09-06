def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.count("a")%2==0]
    lst.sort(key=lambda x: (-x.count("a"), x))
    return lst