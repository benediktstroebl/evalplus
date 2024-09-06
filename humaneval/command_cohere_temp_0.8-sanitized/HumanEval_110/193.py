def exchange(lst1, lst2):
    odd = next((el for el in lst1 if el % 2 != 0), None)
    even = next((el for el in lst2 if el % 2 == 0), None)
    if odd is None or even is None:
        return "YES"
    return "NO"