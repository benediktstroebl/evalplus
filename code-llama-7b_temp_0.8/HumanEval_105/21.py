
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
    # Build a dictionary with number and name, look it up in the by_length method
    by_number = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

    # 1. Take the array and sort it
    sorted_arr = sorted(arr)

    # 2. Reverse the array
    reversed_arr = sorted_arr[::-1]

    # 3. Create a new array to store the names
    final_arr = []

    # 4. Loop over the sorted array and append the name to the final array
    for i in reversed_arr:
        if 1 <= i <= 9:
            final_arr.append(by_number[i])
        else:
            pass

    return final_arr

