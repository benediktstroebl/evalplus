
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
    def by_length(arr):
        arr.sort(reverse=True)
        for i in range(len(arr)):
            arr[i] = [9-x for x in range(1,10) if 9-x == arr[i]][0]
        return arr
    
    def name_by_digit(arr):
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(str(arr[i]) + " " + "One" if arr[i] == 1 else 
                           str(arr[i]) + " " + "Two" if arr[i] == 2 else 
                           str(arr[i]) + " " + "Three" if arr[i] == 3 else 
                           str(arr[i]) + " " + "Four" if arr[i] == 4 else 
                           str(arr[i]) + " " + "Five" if arr[i] == 5 else 
                           str(arr[i]) + " " + "Six" if arr[i] == 6 else 
                           str(arr[i]) + " " + "Seven" if arr[i] == 7 else 
                           str(arr[i]) + " " + "Eight" if arr[i] == 8 else 
                           str(arr[i]) + " " + "Nine")
        return new_arr
    def output(arr):
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(str(arr[i]) + " " + "One" if arr[i] == 1 else 
                           str(arr[i]) + " " + "Two" if arr[i] == 2 else 
                           str(arr[i]) + " " + "Three" if arr[i] == 3 else 
                           str(arr[i]) + " " + "Four" if arr[i] == 4 else 
                           str(arr[i]) + " " + "Five" if arr[i] == 5 else 
                           str(arr[i]) + "
