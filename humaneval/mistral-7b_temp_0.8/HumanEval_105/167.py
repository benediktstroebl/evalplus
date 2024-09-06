
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
    # Your code here
    def num_to_word(n):
        if n == 1: return 'One'
        if n == 2: return 'Two'
        if n == 3: return 'Three'
        if n == 4: return 'Four'
        if n == 5: return 'Five'
        if n == 6: return 'Six'
        if n == 7: return 'Seven'
        if n == 8: return 'Eight'
        if n == 9: return 'Nine'
        return 'Error'

    if not arr: return []
    if any(x < 1 or x > 9 for x in arr): return [num_to_word(arr[0])]

    arr.sort()
    arr.reverse()
    return [num_to_word(x) for x in arr]

