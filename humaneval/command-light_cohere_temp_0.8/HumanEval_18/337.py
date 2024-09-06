Here is a self-contained Python script that defines a function how_many_times that finds the number of occurrences of a substring within a given string. 

```python
import string
def how_many_times(string: str, substring: str):
    return len(string.find(substring))
```

The function uses the find() method from the string module to count the occurrences of the substring in the original string.