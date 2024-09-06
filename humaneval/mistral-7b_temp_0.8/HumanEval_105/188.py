
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
    #sort the integers that are between 1 and 9 inclusive
    arr.sort()
    #reverse the resulting array
    arr.reverse()
    #get the number of elements in the array
    length = len(arr)
    #create a list of strings
    str_list = []
    #for each element in the array
    for i in range(length):
        #append the corresponding name from "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine" to the list
        str_list.append(f"{str(arr[i])}")
    return str_list

