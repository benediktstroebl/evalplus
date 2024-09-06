```python
def is_prime_length(input_str):
    string_length = len(input_str)
    is_prime = True
    
    for i in range(2, int(string_length**0.5)+1):
        if string_length % i == 0:
            is_prime = False
            break
    
    return is_prime

# Test Cases
print(is_prime_length('Hello'))  # Output: True
print(is_prime_length('abcdcba'))  # Output: True
print(is_prime_length('kittens'))  # Output: True
print(is_prime_length('orange'))  # Output: False
```

The above `is_prime_length` function takes an input string, calculates its length, and then checks if this length is prime by iterating from 2 up to the square root of the length. If any divisor is found in that range, it marks the length as composite and breaks out of the loop. If no divisors are found, it considers the length as prime.  This algorithm is efficient `O(Li/2)` since it only needs to check the divisors up to the square root, making it a balanced approach between time and space complexity.  The given test cases in the script validate the function's behavior against the problem statement.  The `print` statements can be commented out once you run the script to see the actual output.  This solution should help pass the tests and solve the problem efficiently for checking whether the string length is a prime number or not.  If you have any questions, let's dive deeper into the code or any other follow-up topics!