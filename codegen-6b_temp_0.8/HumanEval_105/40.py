
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
    else:
        for num in range(len(arr)):
            if arr[num] < 1 or arr[num] > 9:
                arr[num] = None
    arr = [str(elem) for elem in arr if elem != None]
    arr = sorted(arr)
    arr.reverse()
    for num in range(len(arr)):
        if arr[num] == '0':
            arr[num] = 'Zero'
        elif arr[num] == '1':
            arr[num] = 'One'
        elif arr[num] == '2':
            arr[num] = 'Two'
        elif arr[num] == '3':
            arr[num] = 'Three'
        elif arr[num] == '4':
            arr[num] = 'Four'
        elif arr[num] == '5':
            arr[num] = 'Five'
        elif arr[num] == '6':
            arr[num] = 'Six'
        elif arr[num] == '7':
            arr[num] = 'Seven'
        elif arr[num] == '8':
            arr[num] = 'Eight'
        elif arr[num] == '9':
            arr[num] = 'Nine'
    arr = [elem for elem in arr if elem != None]
    return arr

"""
    Given an array of integers, sort the integers by their absolute value in
    descending order. For example, given the array [-1,3,5,-5], the result should be [5,-5,-1,3]
    (or any other list of 4 integers sorted by descending order)
"""