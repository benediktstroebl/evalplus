
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
    # 创建一个空列表，用来存储正确的名称
    names = []
    # 遍历整数数组
    for num in arr:
        if num >= 1 and num <= 9:
            # 将数字转换为字符串并比较为空字符串
            str_num = str(num)
            if len(str_num) == 1:
                # 如果数字只有一个字符，说明是字母
                if str_num == '1':
                    names.append("One")
                elif str_num == '2':
                    names.append("Two")
                elif str_num == '3':
                    names.append("Three")
                elif str_num == '4':
                    names.append("Four")
                elif str_num == '5':
                    names.append("Five")
                elif str_num == '6':
                    names.append("Six")
                elif str_num == '7':
                    names.append("Seven")
                elif str_num == '8':
                    names.append("Eight")
                elif str_num == '9':
                    names.append("Nine")
            else:
                # 如果数字有多个字符，说明不是字母
                names.append("NaN")
        else:
            # 如果数组为空或是空字符串，返回空列表
            return []
    # 返回名称列表
    return names