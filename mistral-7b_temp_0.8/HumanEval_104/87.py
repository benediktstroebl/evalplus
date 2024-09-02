
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # TODO: Write your implementation here
    #check if the digit is even
    def check_digit(n):
        if n % 2 == 0:
            return True
        else:
            return False
    #reverse each number to check if it is even
    def reverse(n):
        if n == 0:
            return n
        return n % 10 + reverse(n // 10)
    #define the return list
    return_list = []
    #for each element
    for i in x:
        #check if the reverse is an even number
        if check_digit(reverse(i)) == False:
            return_list.append(i)
    #sort return list
    return_list.sort()
    return return_list

