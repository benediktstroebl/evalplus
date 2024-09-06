
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    prime_count = 0
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            prime_count = 0
        if string[i] == '2':
            continue
        if string[i] % 2 == 0:
            return False
        if string[i] == '3' and prime_count == 1:
            continue
        if string[i] == '5' or string[i] == '7' or string[i] == '11':
            continue
        if string[i] % 3 == 0:
            return False
        if string[i] == '7' and prime_count == 2:
            continue
        if string[i] == '13' and prime_count == 1:
            continue
        if string[i] % 7 == 0:
            return False
        if prime_count == 3:
            return True
        prime_count += 1
    return False
