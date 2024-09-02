

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    # Step 1: Define a function that returns whether the given number is prime or not.
    def isprime(number):
        if number == 2:
            return True
        elif number % 2 == 0:
            return False
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                return False
        return True
    # Step 2: Define a function that returns the sum of digits of a given number.
    def sum_of_digits(number):
        return sum([int(i) for i in str(number)])
    # Step 3: Take the largest prime from the given list.
    largest = max([i for i in lst if isprime(i)])
    # Step 4: Return the result.
    return sum_of_digits(largest)

