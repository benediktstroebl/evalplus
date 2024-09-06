


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
    
    #in this first iteration of our function we will simply be checking each index of the array, and returning the sum of the array.
    sum = 0
    for i in lst:
        sum += i
    return sum
        



    #in this iteration we will be modifying the list if the index of the list is divisible by 3, and adding the result of that number to our sum
    for i in lst:
        if i % 3 == 0:
            lst[i] = lst[i] * lst[i]
            sum += lst[i]
    return sum



    #for this iteration we will be checking if the index of the list is divisible by 3, and if not, we will be checking if it is divisible by 4
    #if it is divisible by 4, and not 3, we will be cubing the number, and adding it to the sum
    for i in lst:
        if i % 3 != 0:
            if i % 4 == 0:
                lst[i] = lst[i] ** 3
                sum += lst[i]
    return sum




    #for this iteration we will be modifying the list if the index of the list is divisible by 3, and adding the result of that number to our sum
    #for this iteration we will be checking if the index of the list is divisible by 3, and if not, we will be checking if it is divisible by 4
    #if it is divisible by 4, and not 3, we will be cubing the number, and adding it to the sum
    for i in lst:
        if i % 3 == 0:
            lst[i] = lst[i] * lst[i]
            sum += lst[i]
        elif i % 3 != 0:
            if i % 4 == 0:
                lst[i] = lst[i] ** 3
                sum += lst[i]
    return sum
