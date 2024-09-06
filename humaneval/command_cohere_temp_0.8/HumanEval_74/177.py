```python
def total_match(lst1, lst2):
    return lst1 if len(lst1) == len(lst2) else max(set(lst1 + lst2), key=len)
```

The code employs the `len` function to compare the lengths of the two input lists. Subsequently, the `max` function is utilized to select the list with fewer characters, considering duplicate elements as such. To prevent duplicate listings, the `set` function is employed, ensuring only unique combinations are considered. Ultimately, the `key` argument of the `max` function is utilized to prioritize lists based on length, ensuring the list with fewer characters is returned. 

The given example tests outline the functionality of the provided code, showcasing its ability to compare and select lists based on character count. 

This script efficiently solves the problem in a straightforward manner. It is important to note that the script assumes the input lists contain only strings. If the input lists contain elements of different types, additional considerations may be necessary.