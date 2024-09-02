
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Use a dictionary to check if the string is prime or not
    prime_dict = {
        2: [2, 3, 4, 5, 7, 8, 9],
        3: [3, 4, 5],
        5: [5, 7, 9],
        7: [7, 9],
        11: [11],
        13: [13],
        17: [17, 19, 23],
        19: [19, 23],
        23: [23],
        29: [29],
        31: [31, 37],
        37: [37, 41],
        41: [41],
        47: [47],
        53: [53, 59],
        59: [59],
        61: [61, 67],
        67: [67],
        71: [71],
        77: [77],
        83: [83],
        89: [89],
        97: [97],
        101: [101, 103, 107]
    }

    # Check if the string is a prime number
    for i in range(2, len(string) + 1):
        if string[i] == '0':
            continue
        if string[i] in prime_dict[i-1]:
            return False
    return True