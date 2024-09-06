Here's a Python script that contains a function called even_odd_count which takes an integer num as its input and returns a tuple with the counts of even and odd digits in num, as described in the problem:
```python
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if char <= '9' and int(char) % 2 == 0:
                count_even += 1
            elif char <= '9' and int(char) % 2 != 0:
                count_odd += 1
    return (count_even, count_odd)
```

This function converts the integer num to a string num_str to make it easier to directly access each digit in the number. It then iterates through each character in num_str, excluding spaces. For each digit, it checks if it's even or odd using the modulo operator, updates the appropriate count, and then finally returns a tuple of (count_even, count_odd).

Here's a markdown code block with the function for readability:
```python
def even_odd_count(num):
    count_even = 0
    count_odd = 0
    num_str = str(num)
    for char in num_str:
        if char != ' ':
            if char <= '9' and int(char) % 2 == 0:
                count_even += 1
            elif char <= '9' and int(char) % 2 != 0:
                count_odd += 1
    return (count_even, count_odd)
```
You can use this function by providing an integer num as an argument to it, and it will return a tuple with the counts of even and odd digits in num. 

For example:
```python
print(even_odd_count(121))  # (1, 2)
print(even_odd_count(142))  # (2, 1)
print(even_odd_count(345))  # (1, 3)
``` 
This will output:
(1, 2)
(2, 1)
(1, 3)
Which is the count of even and odd digits respectively for the given examples.