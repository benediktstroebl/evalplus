
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
    def length(a):
        ans = 0
        while a is not 0:
            ans += 1
            a //= 10
        return ans

    def arr_to_str(arr):
        ans = []
        for i in arr:
            ans.append(str(i))
        return ''.join(ans)

    def str_to_digit(ans):
        ans = []
        for i in ans:
            ans.append(int(i))
        return ans

    def digit_to_str(arr):
        ans = []
        for i in arr:
            num = i
            if i == 9:
                num = 'Nine'
            elif i == 8:
                num = 'Eight'
            if i == 7:
                num = 'Seven'
            elif i == 6:
                num = 'Six'
            elif i == 5:
                num = 'Five'
            elif i == 4:
                num = 'Four'
            elif i == 3:
                num = 'Three'
            elif i == 2:
                num = 'Two'
            elif i == 1:
                num = 'One'
            ans.append(num)
        return ans

    def digit_to_name(arr):
        ans = []
        for i in arr:
            num = i
            if i == 9:
                num = 'Nine'
            elif i == 8:
                num = 'Eight'
            elif i == 7:
                num = 'Seven'
            elif i == 6:
                num = 'Six'
            elif i == 5:
                num = 'Five'
            elif i == 4:
                num = 'Four'
            elif i == 3:
                num = 'Three'
            elif i == 2:
                num = 'Two'
            elif i == 1:
                num = 'One'
            ans.append(num)
        return ans

    def arr_per_length(arr):
        ans = []
        for i in range(length(arr)):
            ans.append(arr[i])
        return ans

    arr = arr_to_str(