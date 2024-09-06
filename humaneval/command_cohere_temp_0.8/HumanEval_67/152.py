```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operates on two parameters: a string `s` and an integer `n`. This function is designed to solve the problem statement presented in the question. It does so by parsing the given string `s` to extract two important integers: the number of apples and the number of oranges. These are extracted using the `split(' and ')` method, which separates the string at the 'and' delimiter and converts these parts into integers with the `map(int, ...)` approach. Once the numbers of apples and oranges are determined, these values are subtracted from the total number of fruits `n` to obtain the missing number of mango fruits. This calculation is executed through the subtraction operation `n - apples - oranges`. Ultimately, the function returns this calculated amount, signaling the number of mango fruits in the basket.