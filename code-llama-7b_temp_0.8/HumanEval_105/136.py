
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
    # arr = [2, 1, 1, 4, 5, 8, 2, 3] 
    arr = []
    
    if not arr:
      return []
    
    for num in arr:
        if num >= 1 and num <= 9:
            arr.append(num)
            
    sorted_arr = sorted(arr)
    sorted_arr.reverse()
    result = []
    
    for num in sorted_arr:
        if num == 1:
            result.append("One")
        elif num == 2:
            result.append("Two")
        elif num == 3:
            result.append("Three")
        elif num == 4:
            result.append("Four")
        elif num == 5:
            result.append("Five")
        elif num == 6:
            result.append("Six")
        elif num == 7:
            result.append("Seven")
        elif num == 8:
            result.append("Eight")
        elif num == 9:
            result.append("Nine")
            
    return result
    
    #     # create a list of the names
    # names = []
    
    #     # create a list of the numbers
    # numbers = []
    
    #     # add the numbers to numbers list
    # for i in arr:
    #     if i >= 1 and i <= 9:
    #         numbers.append(i)
        
    #     # create a dictionary to match the names with the numbers
    # number_names = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    
    #     # loop through the numbers list and compare to number names
    # for i in numbers:
    #     for key, value in number_names.items():
    #         if i == key:
    #             names.append(value)
                
    # return names
    
    
