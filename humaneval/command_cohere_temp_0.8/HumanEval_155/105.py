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
        raise TypeError("Input must be an integer")
```
The function first checks if the input is an integer, and if so, it converts the integer to a string and then iterates through each digit. It counts the number of even digits and stores it in the count_ev variable and counts the number of odd digits and stores it in the count_od variable. Finally, it returns a tuple containing count_ev and count_od. The raised TypeError ensures that the function only accepts input of type int. 

Here is a simple test case to ensure the function is working:
```python
num = -12
result = even_odd_count(num)
print(result)  # (1, 1)
```
This should print (1, 1) as the test case shows, meaning that there is one even digit and one odd digit in the string representation of -12.