def specialFilter(nums):
    oddDigits = ['1', '3', '5', '7', '9']
    count = 0
    for num in nums:
        if num > 10:
            intVal = int(str(num)[0] + str(num)[-1])
            if intVal and intVal in oddDigits:
                count += 1
    return count