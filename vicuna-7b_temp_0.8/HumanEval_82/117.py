
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Complete code here
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    string_list = string.split()
    for i in range(1, len(string_list)):
        if len(string_list[i]) == 1:
            continue
        for j in range(i+1, len(string_list)):
            if string_list[i] == string_list[j]:
                continue
            if len(string_list[i]) != len(string_list[j]):
                continue
            if is_prime(int(string_list[i]) * int(string_list[j])):
                return True
        if is_prime(int(string_list[i])):
            return True
    return False
