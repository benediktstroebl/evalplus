```python
def how_many_times(string: str, substring: str) -> int:
    """
    Returns count of all occurrences of a given substring in a string. How many times the Gambling a substring
    in the original string.
    Counting is easy in this way: 
    1. Iterate through through string. 
    2. Check if ites substring at each position. 
    3. Return to loop and 
    4.
    Return count of
    times 
    """

    :param string: str, the original string
    :param substring: str, the substring to search for

    :return int: count of all occurrences of the substring
    """

    string = str(string)
    substring = str(substring)

    # converting to lowercase to ensure case insensitivity
    string = string.lower()
    string = substring.lower()

    count = 0

    for i in range(len(string)):
        if string[i] == substring:
            count += 1

    return count

# test code
print(how_many_times('aaaa', 'aa'))
print(how_many_times('Abc', 'a'))
print(how_many_times('A1234bc', '1234'))
```
The above code defines a function `how_many_times` that counts the number of occurrences of a given substring in a string. The function takes two parameters: the original string and the substring to search. The function uses a simple method of iterating over the original string and checking if the current character is the substring. The function then counts the number of times the substring appears and returns the total count.