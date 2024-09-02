


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
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]**2
    else:
        new_lst = lst[0:len(lst):2]
        new_lst = [l**2 for l in new_lst]
        new_lst_2 = lst[1:len(lst):2]
        new_lst_2 = [l**3 for l in new_lst_2]
        return sum(new_lst+new_lst_2)
        
    # lst = [i for i in lst if i%3 == 0 or i%4 == 0]
    # return sum(lst)


assert sum_squares([1, 2, 3]) == 6, "First"
assert sum_squares([]) == 0, "Second"
assert sum_squares([-1, -5, 2, -1, -5]) == -126, "Third"
assert sum_squares([]) == 0, "Fourth"
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 55, "Fifth"
assert sum_squares([1, 2, 3, 4, 5]) == 22, "Sixth"
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, "Seventh"
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 21237, "Eighth"
assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 
                   54, 55, 56, 57, 58, 59, 60,