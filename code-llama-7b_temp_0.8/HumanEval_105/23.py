
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
    # Write your code here
    if len(arr) == 0:
      return []
    
    arr.sort(reverse=True)
    
    sorted_list = []
    for item in arr:
      if item > 0 and item < 10:
        sorted_list.append(str(item))
      elif item == 10:
        sorted_list.append('Ten')
      elif item == 11:
        sorted_list.append('Eleven')
      elif item == 12:
        sorted_list.append('Twelve')
      elif item == 13:
        sorted_list.append('Thirteen')
      elif item == 14:
        sorted_list.append('Fourteen')
      elif item == 15:
        sorted_list.append('Fifteen')
      elif item == 16:
        sorted_list.append('Sixteen')
      elif item == 17:
        sorted_list.append('Seventeen')
      elif item == 18:
        sorted_list.append('Eighteen')
      elif item == 19:
        sorted_list.append('Nineteen')
      elif item == 100:
        sorted_list.append('Hundred')
      elif item == 1000:
        sorted_list.append('Thousand')
      else:
        pass
    
    sorted_list.reverse()
    
    for index, item in enumerate(sorted_list):
      if item == '1':
        sorted_list[index] = 'One'
      elif item == '2':
        sorted_list[index] = 'Two'
      elif item == '3':
        sorted_list[index] = 'Three'
      elif item == '4':
        sorted_list[index] = 'Four'
      elif item == '5':
        sorted_list[index] = 'Five'
      elif item == '6':
        sorted_list[index] = 'Six'
      elif item == '7':
        sorted_list[index] = 'Seven'
      elif item == '8':
