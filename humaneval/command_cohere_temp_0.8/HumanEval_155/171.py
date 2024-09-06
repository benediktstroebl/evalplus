Here's a Python script that contains a function called even_odd_count which takes in an integer and returns a tuple with the number of even and odd digits respectively:
```python
def even_odd_count(num):
    if isinstance(num, int):
        # Remove non-digit characters from the input (assuming this is not an invalid input)
        num_str = str(num).strip('.!')
        count_odd = sum(1 for char in num_str if char % 2 != 0)
        count_even = sum(1 for char in num_str if char % 2 == 0)
        return count_odd, count_even
    else:
        raise ValueError("Input must be an integer")
```

The code assumes that the input is a valid integer and removes non-digit characters (e.g. '!' in the example). It also assumes that the input is not an invalid integer containing non-digit characters.

The function then converts the integer to a string and uses Python's sum function along with a generator expression to count the number of odd and even digits.

Would you like to know more about any of the concepts used in this code?