def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input should be an integer")
    count = 0
    num_str = str(num)
    for char in num_str:
        if char == '0' or char == '1' or char == '2' or char == '3':
            if int(char) % 2 == 0:
                count += 1
        elif char == '4' or char == '5' or char == '6' or char == '7':
            if int(char) % 2:
                count += 1
        elif char == '8' or char == '9':
            if int(char) % 2 == 0:
                count += 1
        else:
            raise ValueError("Unexpected character in input")
    return (count, num_str.count('5'))