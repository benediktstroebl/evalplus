```python
def prime_length(string):
    """
    Check if the string's length is a prime number.
    """
    return notprime(len(string))
# Example usage
string = "abcde123"
print(prime_length(string))  # Output: True
```