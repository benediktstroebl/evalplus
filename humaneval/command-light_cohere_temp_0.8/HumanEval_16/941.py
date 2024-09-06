```python
def count_distinct_characters(string: str):
    """
    Counts the number of distinct characters in the string, regardless of case.
    Args: 
        string: str, a string to evaluate
    Returns: 
        int, the number of distinct characters
    """
    # split string into lowercase and uppercase characters
    lowercase = string.split('')[0]
    uppercase = string.split('')[1]

    # count distinct characters in lowercase and uppercase combined
    distinct = set(lowercase) & set(uppercase)

    return len(distinct)

# Test cases
string1 = 'xyzXYZ'
result1 = count_distinct_characters(string1)
print("Result1:", result1)

string2 = 'jerry'
result2 = count_distinct_characters(string2)
print("Result2:", result2)

``` 
This code defines a function **count_distinct_characters** that counts the number of distinct characters in a given string, regardless of case. It splits the string into lowercase and uppercase characters, counts the distinct characters in the lowercase and uppercase combined, and returns the result.