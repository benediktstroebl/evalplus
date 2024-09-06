
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
    
    # Step 1: Remove invalid integers
    arr = filter(lambda x: x in range(1, 10), arr)
    
    # Step 2: Sort the array
    arr.sort()
    
    # Step 3: Reverse the array
    arr = arr[::-1]
    
    # Step 4: Convert integers to strings and append them to an empty array
    str_arr = [str(x) for x in arr]
    str_arr.append('None')
    
    # Step 5: Make a map
    digit_to_name_map = { 
        "1": "One", 
        "2": "Two", 
        "3": "Three", 
        "4": "Four", 
        "5": "Five", 
        "6": "Six", 
        "7": "Seven", 
        "8": "Eight", 
        "9": "Nine"
    }
    
    # Step 6: Iterate through the map and replace the integers with their names
    for i in range(len(str_arr)):
        if str_arr[i] != 'None':
            str_arr[i] = digit_to_name_map[str_arr[i]]
            
    # Step 7: Return the joined array
    return "".join(str_arr)
