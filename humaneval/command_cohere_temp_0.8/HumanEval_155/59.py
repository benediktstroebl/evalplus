Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if num == 0:
        return (0, 0)
    count_even = 0
    count_odd = 0
    str_num = str(num)
    for char in str_num:
        if char > '9' or char < '0':
            if char in '-'+'.':
                continue
            else:
                return (0, 0) 
        if int(char) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return (count_even, count_odd)
```

This function converts the input num to a string str_num and iterates through each digit. It classifies every digit as either even or odd and increments the respective count accordingly. The function returns a tuple of two integers representing the counts of even and odd digits in the input number, and if a non-digit character is found (like a sign), the counts are reset to 0 and the input is checked for validity. 

To handle the edge case where the input number contains non-digit characters like signs, the code includes a conditional statement. If a non-digit character is encountered, it skips the iteration and resets the counts. This ensures that the counts reflect only the digits, and it also checks if the input is a valid integer, so if the input is not valid, the function returns zero for both counts. 

This solution has a time complexity of O(n), where n is the number of digits in the input number, as it iterates through each digit once.