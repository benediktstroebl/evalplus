
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # your code here
    # convert the string to a list to create a container that is ordered
    # This creates a list in which the characters are grouped together
    my_list = list(string)
    my_list_length = len(my_list)
    my_prime_list = prime_numbers(my_list_length)

    # my_list_length is the length of the string, in this case 6
    # create a list of prime numbers, in this case 2, 3, 5
    # then check if the list of prime numbers includes the length
    # if it does, return true, else return false
    if my_prime_list.count(my_list_length) > 0:
        return True
    else:
        return False

