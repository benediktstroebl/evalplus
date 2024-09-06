```python
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string):
    string = str(string)
    if len(string) <= 1:
        return False
    if is_prime(len(string)):
        return True
    return False
```

The `is_prime` function checks if a given number is prime. It first checks if the number is less than or equal to 3, returning True if so. If the number is greater than 3, it checks if it can be divided evenly by 2 or 3, returning False if so. Next, it begins iterating through numbers beginning with 5, checking for divisibility, and ultimately returning True if the number is prime and False if it is not. 

The `prime_length` function takes a string and returns True if the length of the string is a prime number, and False otherwise. Inside the function, it converts the string to a number to make the length accessible. It then calls the `is_prime` function to check if the length is prime. 

The script effectively solves the problem and would pass the tests provided. You can use it to determine whether or not a given string's length is a prime number. 

You can call the `prime_length` function like this:
```python
prime_length("Hello")  # Should return True
prime_length("abcdcba")  # Should return True
prime_length("kittens")  # Should return True
prime_length("orange")  # Should return False
``` 
This will give you a clear idea of the functionality and correctness of the code.