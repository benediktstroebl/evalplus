Here's a Python script that contains a function called `even_odd_palindrome` which takes in a positive integer `n` and returns a tuple with the count of even and odd integer palindromes within the range(1, n+1), the function is also accompanied by detailed comments to explain each part of the program:
```python
def even_odd_palindrome(n):
    """
    This function calculates the number of even and odd integer palindromes in the range(1, n+1) and returns a tuple containing these counts.
    """

    # Initializing the count of even and odd palindromes to 0
    even_count = 0
    odd_count = 0
    
    # The following loop calculates the number of even and odd palindromes based on the input number n
    for num in range(1, n+1):
        # Checking if the current number is a palindrome by comparing the first and last digits
        if num == int(str(num)[0] + str(num)[-1]):
            # If the number is a palindrome, incrementing the respective count based on its parity
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    # Returning the calculated counts as a tuple
    return (even_count, odd_count)

# Example usage
n = int(input("Enter a number: "))
result = even_odd_palindrome(n)
print(f"Example {n}: (Even: {result[0]}, Odd: {result[1]})")
```

In this code, the `even_odd_palindrome` function iterates through numbers from 1 to `n` (both inclusive) and keeps counts of even and odd palindromes. The `str(num)[0] + str(num)[-1]` is used to convert a number to a string and extract its first and last characters to check if it's a palindrome. The total count is then returned as a tuple.