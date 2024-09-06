Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the count of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int): 
        count_even = 0
        count_odd = 0
        num_str = str(num)
        for char in num_str:
            if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
                count_even += 1
            elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
                count_odd += 1
        return (count_even, count_odd)
    else:  
        raise ValueError("Input must be an integer")
```
The function first converts the input integer into a string, and then checks each digit to count the number of even and odd digits. The final output is returned as a tuple of two integers (count_even, count_odd). This solution works correctly for positive and negative integers and also handles the case where the input is not an integer by raising a ValueError.