```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = set('AEIOU')
    return sum(1 for i, char in enumerate(s) if i % 2 == 0 and char.isupper() and char in vowels)
```

The function uses a set called `vowels` that contains all uppercase vowels. It also utilizes a sum combination to loop through the string. If the character is in the even index, is an uppercase letter, and is a vowel, it gets counted. The total count is then returned. 

This solution has a time complexity of O(n), where n is the length of the string, and a space complexity of O(1) since it only uses a constant amount of extra space. 

To use this code, you can call the function with an example string ('aBCdEf' in the example below), and it will return the number of uppercase vowels in even indices. 

```python
print(count_upper('aBCdEf'))  # 1
``` 
It should be noted that the desired output for the given example is 1, and this code will accurately provide that.