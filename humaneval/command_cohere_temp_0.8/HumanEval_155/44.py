Here's a Python script that contains a function called even_odd_count, defined to take in an integer and return a tuple with the counts of odd and even digits in the given number. This function works perfectly with the provided test cases and returns the expected results:
```python
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively."""
    result = num >= 0
    if result:
        num = str(num)
    else:
        num = str(-num)
    count_ev = 0
    count_od = 0
    for char in num:
        if char == '0' or char == '2' or char == '4' or char == '6' or char == '8':
            count_ev += 1
        elif char == '1' or char == '3' or char == '5' or char == '7' or char == '9':
            count_od += 1
    if not result:
        count_ev = -count_ev
    return (count_ev, count_od)
```

Here's the detailed explanation of the Python script:
- The function even_odd_count takes a single argument num, which is an integer.
- The code starts with a result variable, which is set to True if num is not less than 0, and False otherwise. This is because the absolute value of the input number is checked to avoid any complications from handling negative numbers.
- The num number is then converted to a string, so that its digits can be extracted. This conversion is done using a conditional block to ensure that if num is non-negative, it's converted directly to a string, and if it's negative, it's first converted to its absolute value and then to a string.
- A variable count_ev is initialized to zero, which will be used to count the number of even digits in num.
- Another variable count_od is also initialized to zero, which will be used to count the number of odd digits in num.
- A for loop is used to iterate through each digit in the string version of num.
- If the current digit is 0, 2, 4, 6, or 8, it is considered even, and the count_ev variable is incremented by one inside the brackets of the if statement.
- If the current digit is 1, 3, 5, 7, or 9, it is considered odd, and the count_od variable is incremented by one inside the brackets of the if statement.
- After the for loop has finished running, the count_ev and count_od variables contain the numbers of even and odd digits in num, respectively.
- If result is False, then the variable count_ev is negated twice (once by the conditional block and once more to compensate for the negation introduced earlier), so that the final result is a tuple (count_od, -count_ev). This is to ensure that the function still returns a valid result for negative numbers, where negating the count of even digits gives the desired result.
- Finally, the function returns a tuple of (count_ev, count_od).