def count_nums(arr):
    # Initialise the output sum to 0
    output = 0
    # Use a list comprehension to iterate through each element in 'arr'
    for num in arr:
        # Convert the integer 'num' to a string
        str_num = str(num)
        # Check if the first character of 'str_num' is not '-' to avoid negative numbers
        if str_num[0] != '-':
            # Use a generator expression to sum the digits of 'str_num'
            digit_sum = sum(int(d) for d in str_num)
            # If the digit sum is greater than 0, add num to the output sum
            if digit_sum > 0:
                output += num
    # Return the final output sum
    return output