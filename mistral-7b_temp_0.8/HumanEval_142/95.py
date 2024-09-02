


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

    square_nums = []
    cube_nums = []

    for index, number in enumerate(lst):

        if index % 3 == 0:
            square_nums.append(number * number)
        elif index % 4 == 0:
            cube_nums.append(number * number * number)

    sum_square_nums = 0
    sum_cube_nums = 0

    for number in square_nums:
        sum_square_nums += number

    for number in cube_nums:
        sum_cube_nums += number

    return sum_square_nums + sum_cube_nums

