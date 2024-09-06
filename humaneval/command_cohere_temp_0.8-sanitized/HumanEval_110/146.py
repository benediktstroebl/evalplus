def exchange(lst1, lst2):
    even_numbers = [x for x in lst1 if x % 2 == 0]
    if len(even_numbers) == len(lst1):
        return "YES"
    return "NO"