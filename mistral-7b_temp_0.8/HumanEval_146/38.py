
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] > 10:
            count += 1
            if nums[i] > 0:
                nums_list = str(nums[i])
                first = nums_list[0]
                last = nums_list[-1]
                if first.isdigit() and last.isdigit():
                    if first == '1' or first == '3' or first == '5' or first == '7' or first == '9' or last == '1' or last == '3' or last == '5' or last == '7' or last == '9':
                        continue
                    else:
                        count -= 1
    return count

