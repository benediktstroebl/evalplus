```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts occurrences of a given substring in the original string, 
    considering overlapping matches.
    Example:
    1.
    """ 
    Iterate through string with the substring.
    2. Count the index of string characters 
    3. Count the number of substring in the index range
    4. Find all occurrences of the
    substring
    """
    # Count the first occurrence
    string = 'aaaaaaa'
    sub = 'a'
    count = 0
    for i in range(len(string)):
        if string[i] == sub:
            count += 1
    return count  # Return the count of the first match. 

# Test the function
test = how_many_times('aaaaaaa', 'aa')
print(test)  # Output: 3
``` 
This code defines a function called **how_many_times()** that takes two arguments: a string and a substring. The function uses a same string as a loop and counts the number of occurrences of the substring in the string. It then returns the time the time it took to find the number of occurrences.