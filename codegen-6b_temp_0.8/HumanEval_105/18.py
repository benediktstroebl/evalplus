
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
    def sort_and_reverse(arr):
        arr.sort()

        return arr[::-1]

    def find_digits(arr):
        return [int(s) for s in arr if s in '1234567890']

    def replace_digits(arr, digits):
        replaced = []
        for s in arr:
            if s in '1234567890':
                replaced.append(digits[int(s)-1])
            else:
                replaced.append(s)

        return replaced

    def format_output(arr):
        return ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'][arr]

    return format_output(sort_and_reverse(find_digits(arr)))
