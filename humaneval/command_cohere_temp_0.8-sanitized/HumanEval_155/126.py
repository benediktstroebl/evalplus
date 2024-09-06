def even_odd_count(num):
    if not isinstance(num, int):
        return "ERROR: Input should be an integer"
    
    counts = {True: 0, False: 0}  # Initialize counts dictionary
    
    # Utilize a loop to iterate through each digit in the integer
    for digit in str(num):
        if digit == '0':
            counts[True] += 1
        elif digit == '1':
            counts[True] += 1
        else:
            counts[False] += 1
    
    return counts