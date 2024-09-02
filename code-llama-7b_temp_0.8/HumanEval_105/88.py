
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
    names = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    # 1. Only reverse numbers between 1 and 9 (do not reverse 0)
    # 2. Do not reverse 0
    # 3. do not reverse 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
    # 4. Only reverse numbers from 1 to 9
    # 5. Only reverse numbers between 1 and 9
    def reverse(arr, start, end):
        for x in range(0, len(arr) // 2):
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

    def swap_digits(arr):
        return [str(digit)[::-1] for digit in arr]

    def digit_to_name(arr):
        return ['One' if digit == '1' else 'Two' if digit == '2' else 'Three' if digit == '3' else 'Four' if digit == '4' else 'Five' if digit == '5' else 'Six' if digit == '6' else 'Seven' if digit == '7' else 'Eight' if digit == '8' else 'Nine' if digit == '9' else digit for digit in arr]

    return digit_to_name(reverse(swap_digits(list(filter(lambda x: 0 < x < 10, arr))))[::-1])
