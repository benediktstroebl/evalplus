
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """

    #My Solution
    return (len(string) == 2 or len(string) == 3 or len(string) == 5 or len(string) == 7 or len(string) == 11 or len(string) == 13 or len(string) == 17 or len(string) == 19)

    #Ideas for others:
    #1: use string.length to get the length
    #2: divide the length by 2 to see if there is a remainder
    #3: if there is a remainder, the length is not a prime number
    #4: if there is no remainder, the length is a prime number
    #5: return the result
    #6: if the remainder is 0, return false

    #A way better solution
    return len(string) in (2, 3, 5, 7, 11, 13, 17, 19)


    # Use this to test your function.
    # Any code inside this `if` statement will be ignored by the automarker.
    if __name__ == '__main__':
        print(prime_length('Hello'))
        # should print:
        # True
        print(prime_length('abcdcba'))
        # should print:
        # True
        print(prime_length('kittens'))
        # should print:
        # True
        print(prime_length('orange'))
        # should print:
        # False
