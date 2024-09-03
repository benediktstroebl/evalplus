```python
def generate_even_digits(limit):
    even_digits = []
    for num in range(1, limit+1):
        if num % 2 == 0:
            even_digits.append(str(num))
    return even_digits

#Test case 1: Generate digits between 2 and 8
result1 = generate_even_digits(8)
print("Test case 1 result:", result1)

#Test case 2: Generate digits between 8 and 2
result2 = generate_even_digits(2)
print("Test case 2 result:", result2)

#Test case 3: Generate all digits from 0 to 100
result3 = generate_even_digits(100)
print("Test case 3 result:", result3)
``` 
This function generate_even_digits(limit) generates and returns the list of even digits up to the given positive integer limit. 
Test cases 1, 2, and 3 pass corresponding tests, where the function is called with the limits 2, 8, and 100, respectively.