
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    #for i in range(len(arr)):
     #   nums = [int(n) for n in str(arr[i])]
      #  sums = 0
       # for j in range(len(nums)):
        #    sums += nums[j]
       # if sums > 0:
        #    return len(arr)

    #def count_nums(arr):
        #number = str(arr)
        #sums = 0
        #if number[0] == '-':
         #   number = number[1:]
        #nums = [int(n) for n in number]
        #for i in range(len(nums)):
         #   sums += nums[i]
        #if sums > 0:
         #   return len(arr)
     #   return 0

    #def count_nums(arr):
    #    number = str(arr)
    #    if number[0] == '-':
    #        number = number[1:]
    #    nums = [int(n) for n in number]
    #    sums = sum(nums)
    #    return sums > 0

    #def count_nums(arr):
    #    number = str(arr)
    #    if number[0] == '-':
    #        number = number[1:]
    #    nums = [int(n) for n in number]
    #    return sum(nums) > 0

    def count_nums(arr):
        number = str(arr)
        if number[0] == '-':
            number = number[1:]
        nums = [int(n) for n in number]
        return sum(nums) > 0
