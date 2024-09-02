


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
    # 🚨 Don't change the code above 👆

    #Write your code below this line

    ## Creating new list that contains the squared/cubed elements of lst
    new_lst = []
    for i in range(len(lst)):
        if (i%3==0):
            new_lst.append(lst[i]**2)
        elif (i%4==0 and (i+1)%3 != 0):
            new_lst.append(lst[i]**3)
        else:
            new_lst.append(lst[i])
    ## Creating a new list that contains the sum of new_lst
    sum_new_lst = []
    for i in range(len(new_lst)):
        if (i==0):
            sum_new_lst.append(new_lst[i])
        else:
            sum_new_lst.append(sum_new_lst[i-1]+new_lst[i])

    return sum_new_lst[-1]
    # 🚨 Don't change the code below 👇

    print(sum_squares([1,2,3]), file=f)
    print(sum_squares([]), file=f)
    print(sum_squares([-1,-5,2,-1,-5]), file=f)










































































































































































