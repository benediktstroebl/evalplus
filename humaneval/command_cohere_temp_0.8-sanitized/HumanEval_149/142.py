def sorted_list_sum(lst):
    lst = [str(el) for el in lst if el.count("a")%2==0]
    lst.sort(key=len, reverse=True)
    lst.sort()
    return lst