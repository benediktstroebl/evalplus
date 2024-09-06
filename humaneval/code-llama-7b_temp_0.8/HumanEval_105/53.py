
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
    rv = []

    for n in arr:
        if 0 < n < 10:
            rv.append(n)

    rv.sort()
    rv.reverse()

    for n in rv:
        if n == 1:
            rv[rv.index(n)] = "One"
        if n == 2:
            rv[rv.index(n)] = "Two"
        if n == 3:
            rv[rv.index(n)] = "Three"
        if n == 4:
            rv[rv.index(n)] = "Four"
        if n == 5:
            rv[rv.index(n)] = "Five"
        if n == 6:
            rv[rv.index(n)] = "Six"
        if n == 7:
            rv[rv.index(n)] = "Seven"
        if n == 8:
            rv[rv.index(n)] = "Eight"
        if n == 9:
            rv[rv.index(n)] = "Nine"

    return rv
