Here's a Python script that contains a function called even_odd_count which takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_odd = 0
    count_even = 0
    num_str = str(num)
    for char in num_str:
        if char > '9' or char < '0':
            if char % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        else:
            if int(char) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)
```

This function first establishes the base case of handling an input of 0, where it returns (0, 0) since no digits beyond 9 or 0 are present. It then converts the input num to a string, num_str, to allow for iteration over its characters. It then checks each character to count odd and even digits. If the character is a digit (0-9), it checks whether it's even or odd and updates the counts accordingly. Finally, the function returns a tuple of (count_even, count_odd).

This solution will give the correct counts of even and odd digits for any valid input integer num.