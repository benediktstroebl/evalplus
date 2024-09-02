
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    # Your code here
    prime_nums = []
    n = 1
    while n < len(string):
        i = 2
        prime = True
        while i < n:
            if n % i == 0:
                prime = False
                break
            i += 1
        if prime:
            prime_nums.append(n)
        n += 1
    return len(string) in prime_nums

