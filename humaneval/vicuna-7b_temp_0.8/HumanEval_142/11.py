


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
    
    def safe_square(x):
        if x % 3 == 0:
            return x**2
        else:
            return x**3
    
    def safe_cube(x):
        if x % 4 == 0:
            return x**3
        else:
            return x**2
    
    def sum_squares_helper(lst, i, j, result):
        if i == j:
            result.append(result[-1] + lst[i])
        else:
            if i % 3 == 0:
                result.append(result[-1] + safe_square(lst[i]))
            else:
                if j % 4 == 0:
                    result.append(result[-1] + safe_cube(lst[j]))
                else:
                    result.append(result[-1] + lst[i] + lst[j])
    
    result = []
    sum_squares_helper(lst, 0, len(lst)-1, result)
    return result[0]
