


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


    def square(x):
        """
        This function will take an integer x and return the square of x.

        Examples:
        For x = 2 the output should be 4
        For x = -1 the output should be 1
        """
        return x*x

    def cube(x):
        """
        This function will take an integer x and return the cube of x.

        Examples:
        For x = 2 the output should be 8
        For x = -1 the output should be -1
        """
        return x*x*x

    sum = 0

    for idx, i in enumerate(lst):
        if idx % 3 == 0:
            sum += square(i)
        elif idx % 4 == 0:
            sum += cube(i)
        else:
            sum += i
    return sum





