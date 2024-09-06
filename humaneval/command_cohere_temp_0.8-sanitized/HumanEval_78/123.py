import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # Check if the input string is empty or not
    if num == "":
        return 0

    # Remove all non-hexadecimal and non-prime digits from the string
    cleaned_num = re.sub(r'[^A-Fa-f0-9]', '', num)

    # Convert the hexadecimal string to an integer to easily manipulate the value
    num_int = int(cleaned_num, 16)

    # Loop through each digit in the hexadecimal number
    for digit in str(num_int):
        if digit in hex_digits and int(digit) in primes:
            count += 1

    return count