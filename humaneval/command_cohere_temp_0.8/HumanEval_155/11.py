Here's a Python script that contains a function called even_odd_count that takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        num_str = str(num)
        
        # Iterate through each digit in the number
        for digit in num_str:
            if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8':
                count_even += 1
            elif digit == '1' or digit == '3' or digit == '5' or digit == '7' or digit == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:
        raise ValueError("Input must be an integer")
```

The function first converts the input integer into a string to make it easier to iterate through each digit. It then iterates through each digit and counts them according to whether they are even or odd. Finally, the function returns a tuple that has the counts of even and odd digits respectively. 

Here is a simple test case to check if the function above correct:
```python
assert even_odd_count(123) == (1, 2)
```

The test case above checks if the function `even_odd_count(123)` returns the tuple `(1, 2)` which represents the number of even and odd digits respectively. The markdowns can be removed since they are not necessary for the code block. Let me know if you would like to learn more about the Python concepts used in the function or anything else pertaining to the original problem!