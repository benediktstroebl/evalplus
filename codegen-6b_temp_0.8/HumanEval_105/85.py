
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

    arr.sort()
    arr.reverse()

    d = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine'
    }

    return [d[number] for number in arr]


assert by_length([23, 12, 23, 12, 23, 12, 11, 23]) == ['Three', 'Four', 'Two', 'Two', 'One', 'One', 'One', 'Three']
assert by_length([]) == []
assert by_length([13, 10, 7, 5, 3, 2, 1]) == ['One', 'One', 'Two', 'Two', 'Three', 'Three', 'Four', 'Five']
assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ['One', 'One', 'Two', 'Two', 'Three', 'Four', 'Five', 'Eight']
