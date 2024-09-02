
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    #   If the list is empty don't do anything.
    if not lst:
        return None
        
    answer = lst[0]  #   The first number is the answer
    
    #   For every number in the list
    for index in range(0, len(lst), 2):
        answer += lst[index]
    
    return answer
