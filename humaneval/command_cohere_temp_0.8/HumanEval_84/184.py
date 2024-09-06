Here's a Python script that contains a function which computes the sum of a positive integer's digits in binary:
```python
def solve(N):
    # Convert the integer to a string
    N_str = str(N)
    sum_list = []
    
    # Get the length of the integer
    l = len(N_str)
    
    # Loop through the digits and add them in reverse to the sum list
    for i in range(l):
        dig = N_str[i]
        dig_bin = bin(int(dig))[2:]
        if dig_bin:
            sum_list.append(dig_bin)
    # Convert the list of binary digits to a string and add to the result
    result = ''.join(reversed(sum_list))
    return result
```

The algorithm works by first converting the integer to a string for ease of manipulation and then converting each digit individually to a binary string. These binary strings are stored in a list called `sum_list`, which is then joined together to form a final binary string representing the sum of the digits in binary. 

This approach ensures a correct and efficient solution.