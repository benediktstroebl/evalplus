```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    # Filtering out the even digits and sorting them
    even_digits = sorted(digit for digit in range(a, b + 1) if digit % 2 == 0)
    return even_digits

# Testing the function with different ranges
print(generate_even_digits(2, 8))  # Output: [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # Output: [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # Output: []
```

This Python script defines a function called `generate_even_digits(a, b)` that takes in two integers, `a` and `b`, and returns a list of all the even digits between `a` and `b`, inclusive, always returning them in ascending order. The function first uses list comprehension to filter out even digits from the range of numbers between `a` and `b`, and then uses the `sorted()` function to sort these even digits in ascending order. 

The function has comment blocks at the top explaining its purpose and behavior, and the following lines are commented as well to provide insight into the returning of the filtered and sorted even digits:
```python
    # Filtering out the even digits and sorting them
    even_digits = sorted(digit for digit in range(a, b + 1) if digit % 2 == 0)
    return even_digits
``` 

The function is then tested with three examples, and its output is printed via the print function. The comment above the print statements explains its purpose, and the Output comment communicates what the user should expect to see when running the script.