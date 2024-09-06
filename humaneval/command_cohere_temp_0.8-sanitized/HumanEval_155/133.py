def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError("Input should be an integer")

    count_even = 0
    count_odd = 0

    num_str = str(num)
    
    if num_str.isalpha():
        raise ValueError("Input contains alphabetic characters, only numeric inputs are supported.")

    for char in num_str:
        if char == '0' or char == '1' or char == '2' or char == '3':
            count_odd += 1
        elif char == '4' or char == '5' or char == '6' or char == '7':
            count_even += 1
        elif char == '8' or char == '9':
            count_odd += 1
        elif char == '':
            continue
        else:
            raise ValueError("Input contains invalid numeric characters")

    return count_even, count_odd