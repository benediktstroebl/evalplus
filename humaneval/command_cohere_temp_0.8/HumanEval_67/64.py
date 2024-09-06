```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python **map()** function to convert the text description of apple and orange quantities (extracted as a string `s`) into actual integer values. These quantities represent the number of apples and oranges in the basket. The function then calculates the quantity of mangoes in the basket by subtracting the sum of apples and oranges from the total number of fruits (represented by `n`). This result provides the estimated number of mangoes in the basket.

The `map()` function divides the string into two parts ('apples' and 'oranges') and converts each part into an integer, making it more readable and easier to understand compared to a brute-force split and convert technique.