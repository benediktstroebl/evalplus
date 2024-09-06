def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    
    counts = {True: 0, False: 0}
    num_str = str(num)
    
    for char in num_str:
        if char == '0' or char == '1' or char == '2' or char == '3':
            counts[True] += 1
        elif char == '4' or char == '5' or char == '6' or char == '7':
            counts[False] += 1
        elif char == '8' or char == '9':
            counts[False] += 1
        else:
            raise ValueError("Unexpected digit found")
    
    return counts