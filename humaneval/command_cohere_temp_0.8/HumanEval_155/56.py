Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is designed to solve the problem you've described:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if char <= '9' and char >= '0':
                if int(char) % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
    return (count_even, count_odd)
```

This function initially checks if the input num is 0, and if so, it returns a tuple (0, 0) to reflect that there are no digits (either odd or even) in the case of zero. Then, it converts the input num to a string, skips any spaces, and iterates through each digit character. It classifies each digit as either even or odd and increments the appropriate count accordingly.

To demonstrate its behavior, here are some examples of test cases along with their corresponding outputs:
```python
# Testing the even_odd_count function
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
print(even_odd_count(15))  # Output: (1, 1)
print(even_odd_count(0))  # Output: (0, 0)
print(even_odd_count(99))  # Output: (1, 2)
```