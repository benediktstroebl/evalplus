Here's a Python script that contains a function named `even_odd_palindrome` which solves the problem you've outlined:
```python
def even_odd_palindrome(n):
    # Ensure n is a positive integer
    if n <= 0:
        return "Invalid input for n. Please input a positive integer."

    # Count even and odd length palindromes
    even_count = 0
    odd_count = 0
    
    for i in range(1, n+1):
        # Create a reversed counterpart of i as a string
        reversed_i = str(i)
        reversed_i = reversed_i[::-1]
        
        # Check if the two counterparts are equal to determine if it's a palindrome
        if i == int(reversed_i):
            if len(reversed_i) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    return (even_count, odd_count)

# Example usage
n = int(input("Enter a positive integer: "))
result = even_odd_palindrome(n)
print(f"Example 1: {result}")  # Replace result with the actual output of your function

n = int(input("Enter a positive integer: "))
result = even_odd_palindrome(n)
print(f"Example 2: {result}")  # Replace result with the actual output of your function
```

You have control over the examples and can substitute them with genuine user input and the corresponding output from your function. Just replace the comments with the actual outputs as you process the input.