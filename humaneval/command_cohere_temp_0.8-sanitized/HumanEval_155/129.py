def even_odd_count(num):
    if isinstance(num, int): 
        # Initialize counts for even and odd digits respectively
        count_ev = 0
        count_od = 0
        # Convert the integer to a string (preserving the decimal point)
        str_num = str(num)
        # Iterate through each character in the string representation of the number
        for char in str_num: 
            # If the character is an even digit, increment the count_ev variable
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_ev += 1
            # If the character is an odd digit, increment the count_od variable
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_od += 1
        # Return a tuple of (count_ev, count_od)
        return (count_ev, count_od)
    else:
        return "Error: Please enter an integer!"