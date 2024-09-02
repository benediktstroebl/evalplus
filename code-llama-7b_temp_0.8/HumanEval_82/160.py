
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    #
    # TODO: Write your function here
    #


    # print(len(string))
    for i in range(2, len(string)+1):
        if len(string)%i == 0:
            print('number of letters: ', i)
            print('string: ', string)
            return True
        else:
            print('string: ', string)
            print('number of letters: ', i)
            return False








