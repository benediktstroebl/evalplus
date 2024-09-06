def specialFilter(nums):
    oddDigits = ['1', '3', '5', '7', '9']
    result = sum(1 for num in nums if int(num) > 10 and 
                 (oddDigits.index(str(num)[0]) != -1 or 
                  oddDigits.index(str(num)[-1]) != -1))
    return result