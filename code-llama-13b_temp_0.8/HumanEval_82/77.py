
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    numbers = {"0":0, "1":0, "2":1, "3":1, "4":0, "5":0, "6":0, "7":1, "8":0, "9":0, "10":0, "11":0}
    prime_count = numbers.get(str(len(string)))
    return prime_count
