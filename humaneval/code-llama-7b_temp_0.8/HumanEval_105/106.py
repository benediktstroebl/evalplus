
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # 1st way
    #     arr = sorted(arr, reverse=True)
    #     return ['One' if a==1 else 'Two' if a==2 else 'Three' if a==3 else 
    #             'Four' if a==4 else 'Five' if a==5 else 'Six' if a==6 else 
    #             'Seven' if a==7 else 'Eight' if a==8 else 'Nine' if a==9 else '' for a in arr]
    
    # 2nd way
    return ['One' if a==1 else 'Two' if a==2 else 'Three' if a==3 else 
            'Four' if a==4 else 'Five' if a==5 else 'Six' if a==6 else 
            'Seven' if a==7 else 'Eight' if a==8 else 'Nine' if a==9 else '' for a in arr]
    
