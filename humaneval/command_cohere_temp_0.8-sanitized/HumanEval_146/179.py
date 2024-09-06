def specialFilter(nums):
    oddDigits = ['1', '3', '5', '7', '9']

    return sum(1 for num in nums if num > 10 and (num%10) in oddDigits and (num%100) in oddDigits)