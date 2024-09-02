
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    #takes number of digits of the number
    for i in range(len(str(n))):
        #convert number to string to be able to split and check each digit
        string_n = str(n)
        #creates a new string by removing the last character
        new_string = string_n[0:len(string_n) - 1]
        #new_string + 1 to be able to iterate through the digit
        if new_string[0] == '1' or new_string[-1] == '1':
            #increase the count by 1
            count = count + 1
    return count
