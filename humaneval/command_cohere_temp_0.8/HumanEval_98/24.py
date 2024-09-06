Here's a Python script with a function that solves the problem:
```python
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Use a dictionary to store the number of uppercase vowels in even indices.
    # Initialize it to 0 initially.
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    even_indices = [i for i, char in enumerate(s) if (i % 2 == 0 and char.isupper() and char in vowels)]
    count = sum(1 for _ in even_indices)
    return count
```
This script defines a function `count_upper()` that takes a string as input and counts the number of uppercase vowels in even indices. It then returns the count. 

To do this, it initializes a counter variable and creates a list of vowels to help with the counting process. It uses a list comprehension to identify even indices that contain an uppercase vowel. It then adds to the count variable each time a qualifying vowel is identified in an even index. Finally, it returns the count of uppercase vowels in even indices. 

This code should be copied and pasted into a Python environment or script file and run to see the function in action. Let me know if you would like me to provide additional samples or explain more on the solution approach!