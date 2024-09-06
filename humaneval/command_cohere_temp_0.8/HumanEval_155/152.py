Here's a Python script that contains a function called even_odd_count, defined to solve the problem you've described:
```python
def even_odd_count(num):
    """Return a tuple with counts of even and odd digits."""
    count = 0
    num_str = str(abs(num))
    for char in num_str:
        if char > '9':
            continue
        if char % 2 == 0:
            count += 1
    return (count, num_str.count('1')) if num_str.count('1') > 0 else (count, 0)

# Test Cases
assert even_odd_count(12) == (1, 0)
assert even_odd_count(15) == (2, 0)
assert even_odd_count(108) == (3, 1)
assert even_odd_count(121) == (3, 0)
assert even_odd_count(1000) == (3, 2)
```

This function first obtains the absolute value of the input integer and converts it to a string. It then iterates through each character in the string, counting the number of even digits (excluding any characters that are not digits). The function also counts the number of occurrences of 1, since the number of odd digits can be derived from this. Finally, the function returns a tuple containing the counts of even and odd digits, or even and 0 for odd if no 1 digit was found. 

Note: This solution assumes that the input integer contains only digits. If the input may contain other characters, additional checks and handling will be necessary. 
To test this out, call the function with various inputs and see how it returns the counts of even and odd digits as tuples! P.S.: If you'd like to dive deeper into Python, coding, or specific problem-solving strategies, feel free to ask!