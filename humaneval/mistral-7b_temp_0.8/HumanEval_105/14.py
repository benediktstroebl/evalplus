
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
    """
    # 1: create a new array with the keys 1-9 and the values "One", "Two", etc.
    name_dict = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

    # 2: sort the arr with the built in .sort method
    sorted_arr = arr.sort()
    # 3: reverse the array with the built in .reverse method
    reversed_arr = sorted_arr.reverse()
    # 4: create a new list to hold the sorted array
    new_list = []

    # 5: loop through the arr and add each value to the new list
    for i in reversed_arr:
        new_list.append(name_dict[i])
    # 6: return the new list
    return new_list
    """
    return [name_dict[i] for i in sorted(arr) if 1<=i<=9]
