

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
    # Step 1: Separate the first part before the ':'
    #         and the second part after ':'
    # Step 2: Ceil and Squared the number
    # Step 3: Sum the numbers in the list
    
    first_part = lst[:lst.index(':')]
    second_part = lst[lst.index(':')+1:]
    
    first_part = [int(x) for x in first_part]
    second_part = [int(x) for x in second_part]
    #print(first_part)
    #print(second_part)
    
    for i in range(len(first_part)):
        first_part[i] = int(math.ceil(first_part[i]))**2
    for j in range(len(second_part)):
        second_part[j] = int(math.ceil(second_part[j]))**2
    
    #print(first_part)
    #print(second_part)
    
    return sum(first_part)+sum(second_part)
    
    
