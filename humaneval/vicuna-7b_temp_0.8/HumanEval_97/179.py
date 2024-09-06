
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Check if the input is a negative number
    if b < 0:
        # Convert the number to a string
        str_num = str(abs(b))
        
        # Check if the last digit is a 5
        last_digit = str_num[-1]
        if last_digit == '5':
            # Subtract the number 5 from the string
            str_num = str_num[:-1]
            
            # If the number is a negative number, the unit digit is the 5
            # Otherwise, the unit digit is the first digit
            unit_digit = '5' if b < 0 else int(str_num[0])
            
            # Check if the other number has a leading zero
            other_digit = int(a)
            if str(other_digit)[-1] == '0':
                # If it does, the product is zero
                return 0
            else:
                # Otherwise, the product is the product of the unit digits
                return int(str_num) * int(str(other_digit))
        else:
            # If the last digit is not a 5, the product is zero
            return 0
    else:
        # Convert the number to a string
        str_num = str(a)
        
        # If the other number has a leading zero,
        # the product is zero
        if str_num[-1] == '0':
            return 0
        else:
            # Otherwise, the product is the product of the unit digits
            return int(str_num) * int(str(b))
