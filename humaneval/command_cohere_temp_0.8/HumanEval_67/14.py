```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python int() function to convert the tokens of the string `s` that are separated by the string `and` into integer values. These integers represent the number of apples and oranges. Subsequently, the function subtracts the sum of these integers from the overall number of fruits in the basket (represented by the integer `n`) to find the remaining number of mangoes, which are not mentioned in the given string `s`.

Here is the main function where the above function is used to do the actual calculations:
```python
def fruit_distribution_main():
    import random

    fruits = ["apples", "oranges", "mangoes"]
    fruit_distributions = [
        "{} apples and {} oranges".format(*random.sample(fruits, 2)) for _ in range(10)
    ]

    for distribution in fruit_distributions:
        result_msg = fruit_distribution(distribution, len(distribution))
        print(f"{distribution} -> {result_msg}")

if __name__ == "__main__":
    fruit_distribution_main()
```

This code has imported the random module and used the `random.sample()` function to create ten random combinations of apples and oranges (represented as variables `fruits`) to test the `fruit_distribution()` function. 

Finally, the main function calls  `fruit_distribution_main()` to run the tests. 

Note: This code uses `if __name__ == "__main__":` to ensure that the `fruit_distribution_main()` function is executed only when this script is run directly. This way, the code will work as a module without executing the test function when imported as a module in another Python script.