```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(s) % 3 == 0 and len(letters_set) == len(s) - 2
```

The function uses an interesting approach. At first, we needed to check only two adjacent letters, but this isn't enough, and we should check every three consecutive letters. To do that, we take advantage of sets, where elements are unique, and order isn't important. When we divide the string into triples, we get each tripe's elements are separated from the others. So, if we take the set of all elements of these triples and check that it equals to the set of all letters in the string excluding two adjacent letters, it will correctly answer whether a string is happy or not. 

This approach allows us to have an additional bonus feature; we don't need to iterate through the string and calculate triples manually, instead, we can directly take the set of letters, which is much more time-efficient. 

The resulting code is a self-contained Python script that solves the given problem. You can easily copy and paste it into a Python environment or IDE to test it out.