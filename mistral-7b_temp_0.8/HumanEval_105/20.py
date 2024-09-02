
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
    a = []
    for i in range(len(arr)):
        if arr[i] > 0 and arr[i] <= 9:
            a.append(arr[i])
    if len(a) != 0:
        a = sorted(a)
        a = a[::-1]
        b = []
        for i in range(len(a)):
            if a[i] == 1:
                b.append('One')
            elif a[i] == 2:
                b.append('Two')
            elif a[i] == 3:
                b.append('Three')
            elif a[i] == 4:
                b.append('Four')
            elif a[i] == 5:
                b.append('Five')
            elif a[i] == 6:
                b.append('Six')
            elif a[i] == 7:
                b.append('Seven')
            elif a[i] == 8:
                b.append('Eight')
           
