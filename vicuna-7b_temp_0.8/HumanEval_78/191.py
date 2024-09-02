
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    """
    num = str(num)
    hex_dict = {
        "0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1,
        "8": 1, "9": 1, "A": 1, "B": 1, "C": 1, "D": 1, "E": 1, "F": 1,
        "10": 2, "11": 2, "12": 2, "13": 2, "14": 2, "15": 2, "16": 2,
        "17": 2, "18": 2, "19": 2, "20": 2, "21": 2, "22": 2, "23": 2,
        "24": 2, "25": 2, "26": 2, "27": 2, "28": 2, "29": 2, "30": 2,
        "31": 2, "32": 2, "33": 2, "34": 2, "35": 2, "36": 2, "37": 2,
        "38": 2, "39": 2, "40": 2, "41": 2, "42": 2, "43": 2, "44": 2,
        "45": 2, "46": 2, "47": 2, "48": 2, "49": 2, "50": 2, "51": 2,
        "52": 2, "53": 2, "54": 2, "55": 2, "56": 2, "57": 2, "58": 2,
        "59": 2, "60": 2, "61": 2, "62": 2, "63": 2, "64":
