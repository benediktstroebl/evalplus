
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

    try:
        if arr == []:
            return []
        for i in arr:
            if i not in range(1, 10):
                return []
            else:
                continue
        reverse_array = [i for i in arr if 1 <= i <= 9]
        reverse_array.sort(reverse=True)
        reverse_array = [str(i) for i in reverse_array]
        reverse_array = [i.replace('1', 'One').replace('2', 'Two').replace('3', 'Three').replace('4', 'Four').replace('5', 'Five').replace('6', 'Six').replace('7', 'Seven').replace('8', 'Eight').replace('9', 'Nine') for i in reverse_array]
        return reverse_array
    except:
        return []
