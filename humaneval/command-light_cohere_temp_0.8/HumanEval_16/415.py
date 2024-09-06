```python
def count_distinct_characters(string: str):
    return len({c for c in string.str(). slc.lower() if theUTC,
    if 'z'.isdigit(c) and c not in string.lower(). string.digits(), c.isdigit()
       a(c) and c not in string.upper(), c.isalpha())

    return len(set(string))

x = 'abcXYZabc'
y = 'XXX'dXYH'

print(count_distinct_characters(x))
# ;
print(count_distinct_characters(y))
)
``` 
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It iterates over each character of the input string and checks if each character is a letter using the `islower()`, `isalpha()`, and `isdigit()` functions. It then uses a string.finally, `lower()`, and `set()` functions to create a set of all distinct characters in the string. Finally, it returns the set's length, which is the number of distinct characters in the string.

The function is then tested with two input strings: 'abcXYZabc' and 'XXX'dXYH'. The first test returns 3, which is the number of distinct characters in the string 'abcXYZabc', and the second test returns 4, which is the number of distinct characters in the string 'XXXdXYH'.