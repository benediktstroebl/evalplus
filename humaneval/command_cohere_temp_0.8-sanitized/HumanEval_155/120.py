def even_odd_count(num):
    """Return number of even and odd digits in num."""
    # Convert num to string and remove any non-digit characters
    num_str = str(abs(num)).strip('1234567890.')
    count_odd = count_even = 0
    # Iterate over each character in the string and count the number of odd and even digits
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_odd += 1
    return (count_even, count_odd)