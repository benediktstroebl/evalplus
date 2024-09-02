
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
    arr_new = []
    for i in arr:
        if 1<=i<=9:
            arr_new.append(i)
    arr_new.sort(reverse=True)
    for i in range(len(arr_new)):
        if arr_new[i]==1:
            arr_new[i]="One"
        elif arr_new[i]==2:
            arr_new[i]="Two"
        elif arr_new[i]==3:
            arr_new[i]="Three"
        elif arr_new[i]==4:
            arr_new[i]="Four"
        elif arr_new[i]==5:
            arr_new[i]="Five"
        elif arr_new[i]==6:
            arr_new[i]="Six"
        elif arr_new[i]==7:
            arr_new[i]="Seven"
        elif arr_new[i]==8:
            arr_new[i]="Eight"
        elif arr_new[i]==9:
            arr_new[i]="Nine"
    return arr_new


