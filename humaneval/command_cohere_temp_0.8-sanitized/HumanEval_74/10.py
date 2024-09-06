def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(el) for el in lst1)
    total2 = sum(len(el) for el in lst2)
    
    # If the total character count is less in the second list, return the second list
    if total1 > total2:
        return lst2
    # If the total character count is less in the first list, return the first list
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the first list or second list, whichever has the element 'admin' at the top
    else:
        return ['admin' in el for el in lst1] or ['admin' in el for el in lst2]