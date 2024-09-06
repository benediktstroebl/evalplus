def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.length()%2==0]
    lst.sort(key=lambda x: (x.length(), x))
    return lst