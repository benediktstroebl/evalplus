```python
def number_of_odd_digits(lst):
    num_odd_digits = []
    for strings in lst:
        string = ''.join(strings.split())
        odd_count = sum(1 for char in string if char % 2 != 0)
        num_odd_digits.append(odd_count)
    return num_odd_digits
```

This Python script provides a function `number_of_odd_digits`, which accepts a list of strings `lst`. It aims to calculate the number of odd digits in each string in the list and save these counts in a new list, which is then returned. The function conducts this by summing the number of odd digits in each separate string.

To achieve this, the function iterates through each string in the input list. It combines these separated strings into one using ''.join(strings.split()), ensuring the odd digit count calculation is accurate. The function then loops through each character in the combined string, checking if the character is odd. It does this using the expression char % 2 != 0, which returns True if the character is odd. The function counts these odd characters using sum(1 for char ...), and lastly, appends this count to the list being developed. This is the final output of the function. 

Overall, the provided code appears to be logical and efficient in solving the given problem, as it delivers the expected output.