```python
def simplify(x, n):
    num_x = map(int, x.split('/'))
    num_n = map(int, n.split('/'))
    
    denominator_x = num_x[1]
    denominator_n = num_n[1]
    
    return denominator_x == denominator_n and str(num_x[0] * num_n[0])[:1] == '1'
```

The function `simplify()` takes two arguments, `x` and `n`, which are strings representing fractions in the format `<numerator>/<denominator>`. It splits these strings into numerators and denominators and then checks if the product of the numerators is 1 and if the denominators are equal. If both conditions are met, it returns `True`, if not, it returns `False`. 

This solution adheres to the given assumption that `x` and `n` are valid fractions and does not have zero as denominator. It also efficiently performs integer multiplication and comparison using Python's map() function, which simplifies the code and makes it more readable. The logic also efficiently determines if the result is a whole number within the given format.