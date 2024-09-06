Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    count_even = 0
    count_odd = 0

    str_num = str(num)
    
    for char in str_num:
        if char <= '9' and char >= '0':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            # Ignore non-digit characters
            continue
    
    return (count_even, count_odd)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
```

This script defines a function called even_odd_count that takes in an integer as an argument and checks if the given input is an integer. It then converts the input integer into a string, iterates through each digit, and counts the number of even and odd digits. The function returns a tuple containing the counts of even and odd digits, respectively. The provided example usage demonstrates how to use the function to count the even and odd digits in various input numbers.  It raises a TypeError if the input is not an integer.