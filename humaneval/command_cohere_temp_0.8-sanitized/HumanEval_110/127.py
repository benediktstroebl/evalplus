def exchange(lst1, lst2):
    even_numbers = [x for x in lst1 if x % 2 == 0]
    if len(even_numbers) == len(lst1):
        return "YES"
    else:
        count = 0
        for element in lst1:
            if element in lst2:
                lst1.remove(element)
                lst2.remove(element)
                count += 1
        if count == len(lst1):
            return "YES"
        else:
            return "NO"