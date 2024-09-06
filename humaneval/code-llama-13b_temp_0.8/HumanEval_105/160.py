
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
    # sorting in Python is done by default by the first item in the list, if you want
    # to sort by a different criterion, you need to provide the key for the sort algorithm
    # the key needs to be a function which receives a single parameter - the item in the list
    # and returns the value by which to sort.
    # in our case, we want to sort by the value, so we just need to provide a function that
    # returns the value of each item in the list:
    return [
        'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
    ][::-1] if len(arr) == 0 else [
        'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
    ][::-1][i] for i in sorted(
        range(len(arr)), key=lambda k: arr[k]
    ) if arr[k] >= 1 and arr[k] <= 9

