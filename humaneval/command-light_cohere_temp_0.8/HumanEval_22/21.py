```python
def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 3, 'abc', }, [4, 'five', None]
print(filter_integers(values_test))  # [1, 2, 3, 4]

empty_values = []
print(filter_integers(empty_values))  # []

string_values = ['string', 3, ' Porotype']
print(filter_integers(string_values))  # [3]

non_integer_values = [1, 2, 'three', (])
print(filter_integers(non_integer_values))  # []
``` 
The provided Python script defines a function called **filter_integers** that filters a given list of values, only returning items that are of type **int**. The function first converts all values to be of type **int** and then returns a new list containing only the **int**-type values.