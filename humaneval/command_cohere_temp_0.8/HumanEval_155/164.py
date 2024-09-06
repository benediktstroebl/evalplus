Here's a Python script that contains a function called even_odd_count that takes an integer num as input and returns a tuple with the number of even and odd digits respectively. This function is demonstrated in the following code block:
```python
def even_odd_count(num):
    if not isinstance(num, int):
        raise ValueError, f"Input num is not int. Got {type(num)}"
    if num < 0:
        raise ValueError, "Negative numbers are not accepted."    
    return count_even_odd(str(num))

def count_even_odd(num_str):
    even = 0
    odd = 0
    for char in num_str:
        if char == '0' or char == '2' or char == '4' or char == '6':
            even += 1
        elif char == '1' or char == '3' or char == '5' or char == '7':
            odd += 1
        else:
            raise ValueError, f"Unexpected digit {char} in number {num_str}"
    return even, odd
```

The provided code defines a Python function even_odd_count(num) that calculates the number of even and odd digits in a given integer num. It first checks if num is an integer and if it's negative; if so, it raises a ValueError. Otherwise, it calls the count_even_odd function to process the string representation of num and returns the counts of even and odd digits as a tuple.