
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

    # TODO: Your code goes here
    if not arr:
        return []
    else:
        arr.sort()
        arr.reverse()

    def name_num(num):
        num = str(num)
        if len(num) == 1:
            num = 'One'
        elif len(num) == 2:
            num = 'Two'
        elif len(num) == 3:
            num = 'Three'
        elif len(num) == 4:
            num = 'Four'
        elif len(num) == 5:
            num = 'Five'
        elif len(num) == 6:
            num = 'Six'
        elif len(num) == 7:
            num = 'Seven'
        elif len(num) == 8:
            num = 'Eight'
        elif len(num) == 9:
            num = 'Nine'
        return num

    return [name_num(el) for el in arr]
