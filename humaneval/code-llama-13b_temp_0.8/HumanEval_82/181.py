
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
    prime = []
    if len(string) < 2:
        return False
    for i in range(1,len(string)+1):
        if all([i % num != 0 for num in range(2,i)]):
            prime.append(i)
    if len(string) in prime:
        return True
    else:
        return False
