
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
    
    # Your code here


    # def by_length(arr):
    #     if not arr:
    #         return []
    #     i = 0
    #     while i < len(arr):
    #         if arr[i] >= 1 and arr[i] <= 9:
    #             arr[i] = 'Nine' if arr[i] == 9 else 'Eight' if arr[i] == 8 else 'Seven' if arr[i] == 7 else 'Six' if arr[i] == 6 else 'Five' if arr[i] == 5 else 'Four' if arr[i] == 4 else 'Three' if arr[i] == 3 else 'Two' if arr[i] == 2 else 'One'
    #         else:
    #             arr.remove(arr[i])
    #         i += 1
    #     arr.reverse()
    #     return arr

    # def by_length(arr):
    #     # I love this!
    #     return sorted(filter(lambda x: 1 <= x <= 9, arr), reverse=True)

    # def by_length(arr):
    #     return sorted(filter(lambda x: x in range(1, 10), arr), reverse=True)

    # def by_length(arr):
    #     return sorted([i for i in arr if 1 <= i <= 9], reverse=True)

    # def by_length(arr):
    #     i = 0
    #     while i < len(arr):
    #         if not 1 <= arr[i] <= 9:
    #             arr.pop(i)
    #         else:
    #             i += 1
    #     arr.reverse()
    #     for i in range(len(arr)):
    #         arr[i] = 'One' if arr[i] == 1 else 'Two' if arr[i] == 2 else 'Three' if arr[i] == 3 else 'Four' if arr[i] == 4 else 'Five'
