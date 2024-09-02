


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
    
    def helper(index, value):
        #if index is divisible by 3 then return value^2
        #if index is divisible by 4 then return value^3
        #if index is divisible by 12 then return value^5
        if index%3 == 0:
            return value**2
        if index%4 == 0:
            return value**3
        if index%12 == 0:
            return value**5
        return value

    return sum(map(helper, range(len(lst)), lst))


