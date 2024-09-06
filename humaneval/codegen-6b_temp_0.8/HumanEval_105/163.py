
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
    # use a map to keep track of what number we're seeing
    # without this, we'd have an endless loop
    mapping = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
               6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    if not arr:
        return []
    # split the array into groups of size 3
    groups = []
    for i in range(0, len(arr), 3):
        groups.append(arr[i:i+3])
    # sort and reverse each group
    groups = sorted(groups, reverse=True)
    groups = map(list, groups)
    groups = reversed(groups)
    # join each group back together
    groups = ["".join(group) for group in groups]
    # now map each item to a key
    groups = [mapping[int(i)] for i in groups]
    return groups
