
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
    
    n1 = []
    n2 = []
    n3 = []
    n4 = []
    n5 = []
    n6 = []
    n7 = []
    n8 = []
    n9 = []
    for num in arr:
        if num > 0 and num < 10:
            if num == 1:
                n1.append(num)
            elif num == 2:
                n2.append(num)
            elif num == 3:
                n3.append(num)
            elif num == 4:
                n4.append(num)
            elif num == 5:
                n5.append(num)
            elif num == 6:
                n6.append(num)
            elif num == 7:
                n7.append(num)
            elif num == 8:
                n8.append(num)
            elif num == 9:
                n9.append(num)
                
    l1 = len(n1)
    l2 = len(n2)
    l3 = len(n3)
    l4 = len(n4)
    l5 = len(n5)
    l6 = len(n6)
    l7 = len(n7)
    l8 = len(n8)
    l9 = len(n9)
    length = max(l1, l2, l3, l4, l5, l6, l7, l8, l9)
    names = []
    if length != 0:
        while length > 0:
            if length == l1:
                for num in n1:
                    names.append("One")
            if length == l2:
                for num in n2:
                    names.append("Two")
            if length == l3:
                for num in n3:
                    names.append("Three")
            if length == l4:
                for num in n4:
                    names.append("Four")
            if length == l5:
                for num in n5:
                    names.append("Five")
            if length == l6:
               
