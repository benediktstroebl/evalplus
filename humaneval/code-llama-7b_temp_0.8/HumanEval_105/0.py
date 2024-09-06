
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
    # Write your code here.
    # O(n) time | O(1) space
    # O(n log n) time | O(n) space
    
    def get_name(num):
      if 1 <= num <= 9:
        return [x for x in range(1, 10) if x == num][0]
      
    def get_names(arr):
      sorted_arr = sorted(arr)
      return [get_name(num) for num in sorted_arr[::-1]]
    
    def reverse_map(arr):
      return [x for x in arr[::-1]]
    
    def map_names(arr):
      result = []
      for num in arr:
        if 1 <= num <= 9:
          result.append("One" if num == 1 else "Two" if num == 2 else "Three" if num == 3 else "Four" if num == 4 else 
                        "Five" if num == 5 else "Six" if num == 6 else "Seven" if num == 7 else "Eight" if num == 8 else "Nine")
      return result
    
    result = get_names(arr)
    result = reverse_map(result)
    result = map_names(result)
    
    return result
    
