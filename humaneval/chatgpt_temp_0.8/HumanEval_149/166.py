python
def sorted_list_sum(lst):
    # Remove strings with odd lengths
    lst = [s for s in lst if len(s) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    
    return lst
