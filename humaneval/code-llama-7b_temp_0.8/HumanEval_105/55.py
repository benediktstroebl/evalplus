
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
    
    def get_length(n):
        length = 0
        if n != 0:
            length += 1
        if n % 10:
            n = n // 10
            if n != 0:
                length += 1
            if n % 10:
                n = n // 10
                if n != 0:
                    length += 1
        return length
    
    def get_name(n):
        name = None
        if n % 10:
            name = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][n % 10 - 1]
        return name
    
    def by_length(arr):
        result = []
        for num in arr:
            length = get_length(num)
            name = get_name(num)
            if name and length:
                result.append((length, name))
        return [i[1] for i in sorted(result)]
    
    return by_length(arr)

