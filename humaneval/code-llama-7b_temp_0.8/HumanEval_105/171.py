
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
    def to_name(arr):
        # {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        res = []
        names = {}
        for i in range(1,10):
            names[i] = str(i)
        for i in arr:
            if i in names:
                res.append(names[i])
        return res

    def reverse_names(arr):
        res = []
        for i in range(len(arr)-1, -1, -1):
            res.append(arr[i])
        return res

    def sort_nine(arr):
        res = []
        for i in range(1,10):
            for j in range(len(arr)):
                if i == arr[j]:
                    res.append(i)
        return res

    if len(arr) == 0:
        return arr
    elif len(arr) == 1:
        if arr[0] in range(1,10):
            return to_name(arr)
        else:
            return []
    else:
        arr = sort_nine(arr)
        arr = reverse_names(arr)
        return to_name(arr)

