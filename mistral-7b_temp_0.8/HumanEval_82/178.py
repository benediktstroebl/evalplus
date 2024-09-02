
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    list_len = []
    len_str = len(string)
    for i in range(1,len_str+1):
        list_len.append(i)
    for j in list_len:
        if(j>1):
            for k in range(2,j):
                if(j%k == 0):
                    break
            else:
                return True
        else:
            return False
