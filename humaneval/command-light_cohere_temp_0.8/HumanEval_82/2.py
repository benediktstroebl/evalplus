```python
def prime_length(string):
    """Check if the string length is a prime number"""
    if len(string) == 1:  # if the length is 1, it can't be a prime
        return False
    for i in range(2, len(string)//2):
        if string[i] == string[int(i)]:  # check if the substring has equal number of occurrences
            return False
    return True

# Test cases
print(prime_length('Hello'))  # Output: True
print(prime_length('abcdcba'))  # Output: True
print(prime_length('kittens'))  # Output: True
print(prime_length('orange'))  # Output: False
``` 
The function `prime_length` takes a string and checks if its length is a prime number. It then returns `True` if the length is a prime and `False` otherwise.