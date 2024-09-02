
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
    if len(arr) == 0:
        return []
    #sort the input array
    arr.sort()
    
    #replace the digits with names
    one = ['One','One','One','One','One','One','One','One','One']
    two = ['Two','Two','Two','Two','Two','Two','Two','Two','Two']
    three = ['Three','Three','Three','Three','Three','Three','Three','Three','Three']
    four = ['Four','Four','Four','Four','Four','Four','Four','Four','Four']
    five = ['Five','Five','Five','Five','Five','Five','Five','Five','Five']
    six = ['Six','Six','Six','Six','Six','Six','Six','Six','Six']
    seven = ['Seven','Seven','Seven','Seven','Seven','Seven','Seven','Seven','Seven']
    eight = ['Eight','Eight','Eight','Eight','Eight','Eight','Eight','Eight','Eight']
    nine = ['Nine','Nine','Nine','Nine','Nine','Nine','Nine','Nine','Nine']
    
    #create a new array to store the output
    out = []
    
    #iterate through the input array
    for num in arr:
        if num in range(1,10):
            out.append(one[num-1])
        elif num in range(10,20):
            out.append(two[num-10])
        elif num in range(20,30):
            out.append(three[num-20])
        elif num in range(30,40):
            out.append(four[num-30])
        elif num in range(40,50):
            out.append(five[num-40])
        elif num in range(50,60):
            out.append(six[num-50])
        elif num in range(60,70):
            out.append(seven[num-60])
        elif num in range(70,80):
            out.append(eight[num-70])
        elif num in range(80,90):
            out.append(nine[num-80])
    
    #reverse the output array
    out.reverse()
    
