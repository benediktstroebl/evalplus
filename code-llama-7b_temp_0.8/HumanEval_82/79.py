
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # In this case, I decided to use a dictionary, as I thought it was the best option
    # to check all the values.

    # I created a list of the common prime numbers up to 100 (that are the values that
    # have been used to solve the exercise).
    prime_values = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    # I created a list to store all the values of the length of the input string.
    length = []

    # Then I used a for loop to get the values and append them into the length list
    for i in range(len(string)):
        length.append(string[i])

    # Finally, I used the length list and if condition to check if the values are in the prime_values list.
    for i in length:
        if i in prime_values:
            return True
        else:
            return False

