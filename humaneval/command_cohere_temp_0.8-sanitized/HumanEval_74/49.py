def total_match(lst1, lst2):
    # Calculate the total character count in lst1 and lst2
    total1 = sum(len(val) for val in lst1)
    total2 = sum(len(val) for val in lst2)
    
    # If the total character count of lst2 is less than lst1, return lst2
    if total1 > total2:
        return lst2
    # If the total character count of lst1 is less than lst2, return lst1
    elif total2 > total1:
        return lst1
    # If the total character counts are the same, return the first list lst1
    else:
        return lst1