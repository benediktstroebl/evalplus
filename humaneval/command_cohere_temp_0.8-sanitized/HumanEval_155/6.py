def even_odd_count(num):
    def digit_count(num):
        # Convert the integer to a string
        num_str = str(num)
        # Initialize the count of even and odd digits to 0
        even_count = odd_count = 0
        # Iterate over each digit in the integer
        for digit in num_str:
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return even_count, odd_count
    
    if num == 0:
        return (0, 0)  # Handle the special case of zero
    else:
        return digit_count(num)