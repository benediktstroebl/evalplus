
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
    # Initialize the reverse array
    reverse = []

    # If the array is empty
    if len(arr) == 0:
        return reverse
    
    # Filter out numbers that are not between 1 and 9
    for item in arr:
        if (item >= 1) and (item <= 9):
            reverse.append(item)
    reverse.reverse()
    reverse = [str(i) for i in reverse]

    # Convert integers to words
    for i in range(len(reverse)):
        if reverse[i] == "1":
            reverse[i] = "One"
        elif reverse[i] == "2":
            reverse[i] = "Two"
        elif reverse[i] == "3":
            reverse[i] = "Three"
        elif reverse[i] == "4":
            reverse[i] = "Four"
        elif reverse[i] == "5":
            reverse[i] = "Five"
        elif reverse[i] == "6":
            reverse[i] = "Six"
        elif reverse[i] == "7":
            reverse[i] = "Seven"
        elif reverse[i] == "8":
            reverse[i] = "Eight"
        elif reverse[i] == "9":
            reverse[i] = "Nine"
    
    return reverse
