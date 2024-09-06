
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
    result = []
    for i in sorted(arr):
        if i >= 1 and i <= 9:
            result.append(str(i))
    for i in reversed(result):
        result[result.index(i)] = str(i) + " " + str(int(i) - 1) + " " + str(int(i) - 2) + " " + str(int(i) - 3) + " " + str(int(i) - 4) + " " + str(int(i) - 5) + " " + str(int(i) - 6) + " " + str(int(i) - 7) + " " + str(int(i) - 8) + " " + str(int(i) - 9)
    for i in result:
        result[result.index(i)] = i.split()
    for i in range(len(result)):
        for j in result[i]:
            if j == "1":
                result[i][result[i].index(j)] = "One"
            elif j == "2":
                result[i][result[i].index(j)] = "Two"
            elif j == "3":
                result[i][result[i].index(j)] = "Three"
            elif j == "4":
                result[i][result[i].index(j)] = "Four"
            elif j == "5":
                result[i][result[i].index(j)] = "Five"
            elif j == "6":
                result[i][result[i].index(j)] = "Six"
            elif j == "7":
                result[i][result[i].index(j)] = "Seven"
            elif j == "8":
                result[i][result[i].index(j)] = "Eight"
            elif j == "9":
                result[i][result[i].index(j)] = "Nine"
    for i in result:
        i.append(i.pop())
    for i in result:
        i.append(i.pop())
    for i in result:
       
