
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
    if not arr:
        return []

    def char(n):
        if n == 1:
            return "One"
        if n == 2:
            return "Two"
        if n == 3:
            return "Three"
        if n == 4:
            return "Four"
        if n == 5:
            return "Five"
        if n == 6:
            return "Six"
        if n == 7:
            return "Seven"
        if n == 8:
            return "Eight"
        if n == 9:
            return "Nine"

    res = []
    for i in range(1, 10):
        res.append(char(i))
    arr.sort(reverse=True)
    new_arr = []
    for i in arr:
        if i not in res:
            new_arr.append("One")
        else:
            new_arr.append(res[res.index(i)])
    return new_arr

