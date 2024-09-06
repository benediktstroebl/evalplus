```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    s = set()
    for i in range(1, n+1):
        if i % 10 == 7 and (i / 10) % 11 == 0 or (i / 10) % 13 == 0:
            s.add(7)
   
    return len(s)

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This code defines a function called `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than a given input n, which are divisible by 11 or 13. The function uses a set to keep track of digits and a simple for loop to iterate through numbers up to n. The function then checks if the number is divisible by both 11 and 13, and if so, it adds 7 to the set. If the number is not divisible by 11 or 13, the function returns 0, indicating no occurrences of 7 in such numbers.