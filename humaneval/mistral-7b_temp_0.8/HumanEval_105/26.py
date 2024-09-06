
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
    # TODO: Write your code here
    if arr == []:
        return []
    else:
        arr1 = []
        for i in range(len(arr)):
            if arr[i] < 10:
                arr1.append(arr[i])
        arr1.sort()
        arr1.reverse()
        arr2 = []
        for j in range(len(arr1)):
            if j < 10:
                arr2.append(arr1[j])
        arr3 = []
        for i in range(len(arr2)):
            if i < 10:
                arr3.append(num_to_word(arr2[i]))
        return arr3

