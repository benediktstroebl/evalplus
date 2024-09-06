
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
    # your code here
    # arr=sorted(arr)
    # arr=arr[::-1]
    # print(arr)
    # arr.sort()
    # print(arr)
    # for i in arr:
    #   if 1<=i<=9:
    #     print(i)
    # for i in range(0,len(arr)):
    #     arr[i] = int(arr[i])

    # print(arr)
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if 1<=arr[i]<=9:
                print(arr[i])
                print(type(arr[i]))
                break
            else:
                continue

    # for i in arr:
    #     if i!=1 and i!=2 and i!=3 and i!=4 and i!=5 and i!=6 and i!=7 and i!=8 and i!=9:
    #         arr.remove(i)

    # print(arr)


    # for i in arr:
    #     if 1<=i<=9:
    #         print(i)
    #         arr.remove(i)
    #     else:
    #         continue












