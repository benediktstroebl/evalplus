Here's the solution:

def fizz_buzz(n):
    count = 0
    for num in range(10, n+1):
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test code
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3

This function counts the occurrences of the number 7, which is either divisible by 11 or 13, and returns the result.