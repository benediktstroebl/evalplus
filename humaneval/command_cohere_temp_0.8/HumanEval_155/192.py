Here's a Python script with a self-contained function that solves the problem:
```python
def even_odd_count(num):
    res = str(num).split("")
    even, odd = 0, 0
    for x in res:
        if x[0] % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd
```

This script defines a function even_odd_count(num) that takes an integer num as input and returns a tuple containing the counts of even and odd digits in num. The script splits the string representation of the input number into individual digits, then iterates through each digit, counting them while classifying them as 'even' or 'odd' based on their first digit. Finally, it returns a tuple of these two counts. 

To follow the problem statement exactly, the script assumes that the input is an integer type (e.g., -12, 123, 34567). If the input is not an integer, the function may not return the expected results.  If you have specific scenarios in mind that involve input types other than integers, I can adjust the function to handle those cases accordingly.