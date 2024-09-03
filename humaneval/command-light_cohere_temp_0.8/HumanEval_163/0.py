```python
def generate_even_digits(limit):
    digits = []
    while True:
        digit = str(len(str(limit)) + 1).0)
        if len(digit) == len(limit) or int(digit) > limit:
            break
        digits.append(digit)
    return digits
```

This script defines a function generate_even_digits that takes a positive integer limit as an argument. It initializes an empty list 'digits' to store the even digits between 0 and the given limit. The function then enters a loop that generates a digit between 0 and the limit, checks if the length of the string representation of the current limit value is equal to the limit or greater than the limit, and if so, the loop breaks. The even digits are then appended to the 'digits' list.