
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    n = len(nums)
    # Create a 2D array to store the sum of digits for each number
    # 0 represents invalid input (not a number)
    # 1, 2, 3, ..., digits of number - 1
    # 10 represents the invalid number itself
    # 11 represents the invalid number with all digits 1
    # 12 represents the invalid number with all digits 2
    # ...
    # 100 represents the invalid number with all digits 0
    sum_of_digits = [['']*10 for _ in range(10)]

    # Push invalid inputs to the right
    for i in range(n):
        if not isinstance(nums[i], int):
            sum_of_digits[nums[i]-'0'] = ['']*10
            continue

    for i in range(n):
        # Scan the number and update sum_of_digits
        j = 0
        while nums[i] != '0':
            sum_of_digits[nums[i]-'0'][j] = nums[i]-'0'
            j += 1
            nums[i] = nums[i]//10
        nums[i] = nums[i]%10
        # If we have reached the end of the list, we are done
        if j > 0:
            break
        # Otherwise, the number is too big and we need to start over
        # with the next number in the list

    result = []
    # Create a list to store the digit of the number
    # The number of digits of the number is the first element
    # and subsequent elements store the digit of the number
    # The last element is reserved for the invalid number
    digits_of_number = [0] * 11
    for i in range(n):
        # Push invalid inputs to the right
        if not isinstance(nums[i], int):
            digits_of_number[nums[i]-'0'] = [0] * 10
            continue
        # Update digits_of_number
