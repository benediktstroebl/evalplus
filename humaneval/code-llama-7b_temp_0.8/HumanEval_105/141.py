
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
    rev = []
    for item in arr:
        if item < 10 and item > 0:
            rev.append(item)
    rev.sort(reverse=True)
    print(rev)
    for i in range(len(rev)):
        if rev[i] == 1:
            rev[i] = "One"
        elif rev[i] == 2:
            rev[i] = "Two"
        elif rev[i] == 3:
            rev[i] = "Three"
        elif rev[i] == 4:
            rev[i] = "Four"
        elif rev[i] == 5:
            rev[i] = "Five"
        elif rev[i] == 6:
            rev[i] = "Six"
        elif rev[i] == 7:
            rev[i] = "Seven"
        elif rev[i] == 8:
            rev[i] = "Eight"
        elif rev[i] == 9:
            rev[i] = "Nine"
    return rev
