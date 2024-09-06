Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_ev = 0
        count_od = 0
        str_num = str(num)
        for char in str_num: 
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_ev += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_od += 1
        return (count_ev, count_od)
    else:
        return "Error: Please enter an integer!"
```

And here is a markdown code block with inline comments that describe the functionality of the code:
```python
# Convert the given number to a string so that we can iterate through each digit
def even_odd_count(num):
    if isinstance(num, int): 
        # Initialize counts for even and odd digits respectively
        count_ev = 0
        count_od = 0
        # Convert the integer to a string (preserving the decimal point)
        str_num = str(num)
        # Iterate through each character in the string representation of the number
        for char in str_num: 
            # If the character is an even digit, increment the count_ev variable
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_ev += 1
            # If the character is an odd digit, increment the count_od variable
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_od += 1
        # Return a tuple of (count_ev, count_od)
        return (count_ev, count_od)
    else:
        return "Error: Please enter an integer!"
```

This implementation takes an integer num as input and returns a tuple of two counts: one for even digits and one for odd digits. The program works as follows:
1. Convert the given number to a string so that we can iterate through each digit.
2. Initialize two counters, count_ev and count_od, both set to zero, to keep track of the number of even and odd digits respectively.
3. Iterate through each character in the string representation of the number.
4. If the character is an even digit (0, 2, 4, 6, 8), increment count_ev.
5. If the character is an odd digit (1, 3, 5, 7, 9), increment count_od.
6. After iterating through all digits, return a tuple of (count_ev, count_od).