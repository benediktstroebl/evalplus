
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
    if len(arr) == 0:
        return []
    if not any(str(x) in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] for x in arr):
        return []
    sorted_arr = sorted(arr)
    name_list = []
    for i in range(len(sorted_arr)):
        name = "One"
        for j in range(sorted_arr[i]-1, len(sorted_arr)):
            name = name + " " + str(sorted_arr[j])
        name_list.append(name.strip())
    return name_list
