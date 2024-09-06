def exchange(lst1, lst2):
    even_index = [i for i, n in enumerate(lst1) if n % 2 == 0]
    if len(even_index) != len(lst1):
        return "NO"
    lst1_copy = [element for element in lst1]
    for idx in even_index:
        lst1[idx] = lst2[idx]
    for idx, element in enumerate(lst2):
        if element % 2 == 0:
            lst1[idx] = lst1_copy[idx]
            return "YES"
    return "NO"