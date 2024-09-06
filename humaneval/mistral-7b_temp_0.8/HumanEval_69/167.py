
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # write your code here
    # 1. find the frequency of each integer
    # 2. compare each integer with its frequency
    # 3. return the greatest integer which frequency >= its value
    # 4. if no such a value exist, return -1
    # 5. if there is more than one value, return the smallest one


    # dictionary: { integer: frequency }
    #sorted: return the integers and the frequency in a tuple: ( integer, frequency )
    # max: return the max frequency
    # if: check if the frequency >= the integer
    # return: the max frequency that satisfy the if condition

    result = {}
    for integer in lst:
        if integer in result:
            result[integer] += 1
        else:
            result[integer] = 1
    sorted_list = sorted(result.items(), key=lambda x: x[1])
    max_freq = sorted_list[-1][1]
    for integer, frequency in sorted_list:
        if frequency >= integer:
            return integer
    return -1
