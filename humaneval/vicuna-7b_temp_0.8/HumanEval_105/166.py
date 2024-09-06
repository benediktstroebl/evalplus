
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
    from itertools import permutations
    from heapq import heappush, heappop

    n = len(arr)

    def count(x):
        count = 0
        for y in arr:
            if x == y:
                count += 1
        return count

    def merge(a, b):
        if count(a) > count(b):
            return a
        else:
            return b

    stack = []
    name_dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    for i in range(n):
        if i == 0 or i == n - 1:
            stack.append(arr[i])
        elif arr[i] < arr[i-1]:
            while stack and stack[-1] < arr[i]:
                popped = heappop(stack)
                name = name_dict[popped]
                stack.append(name)
            stack.append(arr[i])

    return [name_dict[x] for x in stack]