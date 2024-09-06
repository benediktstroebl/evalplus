Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    def digit_count(num):
        # Convert the integer to a string
        num_str = str(num)
        # Initialize the count of even and odd digits to 0
        even_count = odd_count = 0
        # Iterate over each digit in the integer
        for digit in num_str:
            if digit % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return even_count, odd_count
    
    if num == 0:
        return (0, 0)  # Handle the special case of zero
    else:
        return digit_count(num)
```

This script provides a function that achieves the goal of counting even and odd digits in an integer and handles the edge case of input being zero. You can use the even_odd_count function by providing an integer num as a parameter to retrieve the corresponding count of even and odd digits. Feel free to adapt this code to your needs. Let me know if you would like me to explain any part of it in more detail.