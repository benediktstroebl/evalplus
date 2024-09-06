

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    

    """
    # Your code here
    def is_positive(lst):
        for num in lst:
            if num < 0:
                return False
        return True
    
    def round_upper(lst):
        for num in lst:
            num = round(num)
            if is_positive(lst) == False:
                num = int(num)
            lst[lst.index(num)] = num
        return lst
    
    lst = list(lst)
    if is_positive(lst):
        lst = round_upper(lst)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            lst[i] += lst[j]
            lst[j] = lst[j] - lst[i]
    
    return sum(lst)