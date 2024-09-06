

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
    #I use the int() function to round up the numbers
    
    #Use a for loop to loop over the list
    #Make an empty list
    #Use the int() function to round up each element in the list
    #Square each element and add the result to the empty list
    #Use sum() function to find the sum of the elements in the list
    
    #Write your code here
    lst= [int(x) for x in lst]
    square_lst=[]
    for x in lst:
        square=x**2
        square_lst.append(square)
    return(sum(square_lst))
    
    
    
    
    
    
    
    
    
    
