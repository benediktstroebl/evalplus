


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
    #lst = [1,2,3]
    #print(sum_squares(lst))
    #lst = []
    #print(sum_squares(lst))
    #lst = [-1,-5,2,-1,-5]
    #print(sum_squares(lst))
    #lst = [5]
    #print(sum_squares(lst))
    
    multiples_of_3 = [0] * (len(lst) - 1)
    multiples_of_4 = [0] * (len(lst) - 1)
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            multiples_of_3[i] += lst[i]
        elif lst[i] % 4 == 0:
            multiples_of_4[i] += lst[i] ** 3
        else:
            multiples_of_3[i] += lst[i] ** 2
            multiples_of_4[i] += lst[i] ** 2
    result = 0
    for i in range(len(lst)):
        result += multiples_of_3[i] + multiples_of_4[i]
    return result
