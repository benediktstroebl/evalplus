
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
    #your code here
    # raise NotImplementedError()
    # transform integers into names
    # Note: in order to avoid using an if statement, make the names of the numbers equal to their number.
    # Then, after running your array through the sort function, the number will be placed at the correct
    # index.
    name_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    # adapted from https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python
    sort_array = sorted(range(len(arr)), key=lambda k: arr[k])[::-1]
    # adapted from https://stackoverflow.com/questions/35136047/python-get-the-values-of-sorted-list-keys
    sort_names = [name_dict[arr[x]] for x in sort_array]
    return sort_names

