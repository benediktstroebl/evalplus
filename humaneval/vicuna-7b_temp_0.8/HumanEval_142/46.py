


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    lst = [x for x in lst if x != 0]  # remove the zeroes
    even_lst = [lst[i:i+2] for i in range(len(lst)-1)]  # split the list into pairs of consecutive elements
    odd_lst = [lst[i] for i in range(len(lst)-1)]  # split the list into odd elements
    even_sum = 0
    odd_sum = 0
    for e in even_lst:
        e = [x**2 if i % 3 == 0 else x**3 if i % 4 == 0 else x for x in e]
        even_sum += sum(e)
    for o in odd_lst:
        o = [x**2 if i % 3 == 0 else x**3 if i % 4 == 0 else x for x in o]
        odd_sum += sum(o)
    return even_sum + odd_sum