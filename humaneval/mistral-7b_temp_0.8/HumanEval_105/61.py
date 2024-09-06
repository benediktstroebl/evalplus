
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
    # your code here
    if not arr:
        return []

    if not arr[0].isdigit():
        return [str(arr[0])]

    nums = [i for i in arr if i.isdigit()]
    nums.sort()
    nums.reverse()

    ans = []
    for i in nums:
        if i == '1':
            ans.append('One')
        elif i == '2':
            ans.append('Two')
        elif i == '3':
            ans.append('Three')
        elif i == '4':
            ans.append('Four')
        elif i == '5':
            ans.append('Five')
        elif i == '6':
            ans.append('Six')
        elif i == '7':
            ans.append('Seven')
        elif i == '8':
            ans.append('Eight')
        elif i == '9':
            ans.append('Nine')

    return ans
